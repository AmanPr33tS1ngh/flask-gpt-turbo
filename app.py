from flask import Flask, request, render_template, url_for
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.form.get("message")
    client = OpenAI(
        api_key=os.environ.get('OPENAI_KEY'),
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    choices = response.choices
    chat_completion = choices[0]
    bot_response = chat_completion.message.content
    return render_template("chatbot.html", bot_response=bot_response, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True, port=8000)