# CHATBOT
# LLM Chatbot with Flask and SQLite

This project is a chatbot application built using a large language model (LLM). The chatbot allows users to interact with an AI through a web interface, with conversations stored in an SQLite database for history. It is built using Flask for the backend, HTML/CSS for the frontend, and SQLAlchemy to manage the SQLite database.

## Features
- Chat interface using HTML/CSS for a simple, dark-themed UI.
- Flask as the backend framework for routing and handling logic.
- LLM-based chatbot that generates responses based on user inputs.
- SQLite database to store chat history between users and the chatbot.
- Efficient use of a quantized transformer model (via CTransformers) for low-resource hardware.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Database**: SQLite (managed via SQLAlchemy)
- **LLM**: Transformer-based model using the `CTransformers` library

## Project Structure

```plaintext
├── app.py                # Main Flask application
├── templates
│   └── app.html          # Frontend HTML template
├── static
│   └── style.css         # Custom CSS for the frontend
├── chatbot.db            # SQLite database file
├── models.py             # Database models (Chat history)
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
##hugging face model
- **pretrained**- model from hugging face
