#import the needed required libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os

app = Flask(__name__)

# Configure SQLite Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'chatbot.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a database model for storing chat messages
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(500), nullable=False)
    bot_response = db.Column(db.String(500), nullable=False)


with app.app_context():
    db.create_all()

# LLM Configuration
llm = CTransformers(model="TheBloke/Llama-2-7B-Chat-GGML", model_file='llama-2-7b-chat.ggmlv3.q2_K.bin', callbacks=[StreamingStdOutCallbackHandler()])

template = """
[INST] <<SYS>>
You are a helpful, respectful, and honest assistant. Your answers are always brief. and add the role as a chatbot yourself.
<</SYS>>
{text}[/INST]
"""
prompt = PromptTemplate(template=template, input_variables=["text"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

@app.route('/', methods=['GET', 'POST'])
def chat():
    # for database fetch
    previous_chats = ChatHistory.query.all()

    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input.lower() in ["quit", "exit", "bye"]:
            response = "Goodbye!"
        else:
            # Get the response from the chatbot
            response = llm_chain.run(user_input)

        #chatbot saving
        chat_entry = ChatHistory(user_message=user_input, bot_response=response)
        db.session.add(chat_entry)
        db.session.commit()

        # For  updating the previous history
        previous_chats = ChatHistory.query.all()

        return render_template('app.html', user_input=user_input, response=response, chats=previous_chats)

    # For GET requests, simply render the page with the existing chat history
    return render_template('app.html', chats=previous_chats)

if __name__ == '__main__':
    app.run(debug=True)
