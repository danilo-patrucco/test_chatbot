from flask import Flask, render_template, request
import nltk
import re
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define chatbot patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Greetings!"]),
    (r"what is your name?", ["You can call me ChatBot.", "I'm ChatBot!"]),
    (r"how are you?", ["I'm good. How about you?", "I'm doing well, thank you!"]),
    (r"quit", ["Bye!", "Goodbye!"]),
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot.respond(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)

