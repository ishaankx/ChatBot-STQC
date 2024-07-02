# ChatBot-STQC

ChatBot-STQC is a Flask-based chatbot application for handling customer queries using natural language processing.

## Features
* **Interactive Chat Interface:** Engage with users through a web-based chat interface.
* **Natural Language** Processing: Utilizes NLTK and Transformers for understanding user queries.
* **Persistent Storage:** Stores conversation history and user data using SQLite database.
* **Deployment-Ready:** Easily deployable to AWS EC2 for public access.

## Requirements

#### Ensure you have the following installed:

* Python 3.7 or higher
* Dependencies listed in **requirements.txt**

## Installation

1. Clone the repository:

   `git clone https://github.com/ishaankx/ChatBot-STQC.git`

   `cd ChatBot-STQC`


2. Install dependencies:

   `pip install -r requirements.txt`


3. Set up the Flask application:

    `export FLASK_APP=app.py`

    `export FLASK_ENV=development  # Optional: Set to 'production' for production deployment`


4. Run the application:

   `flask run`

Access the application at http://localhost:5000 in your web browser.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

