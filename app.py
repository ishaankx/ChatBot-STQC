import torch
from chat import get_response, bot_name
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
print("Template folder:", os.path.abspath(app.template_folder))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/get', methods=['POST'])
def chat():
    msg = request.form.get("msg")
    response = get_response(msg)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
