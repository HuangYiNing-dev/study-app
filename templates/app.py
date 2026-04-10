from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "system", "content": "你是一个严格的背书考官"},
                {"role": "user", "content": question}
            ]
        }
    )

    result = response.json()
    return jsonify(result)

if __name__ == "__main__":
    app.run()
