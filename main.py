import sys
import os
import openai

from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from flask import Flask, request

app = Flask(__name__)
os.environ.get('OPENAI_API_KEY')

@app.route("/")
def index():
    return '''
        <form action="/answer" method="post">
            What do you want to ask Fish? <input type="text" name="question">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/answer", methods=["POST"])
def answer():
    index = GPTSimpleVectorIndex.load_from_disk('data/index.json')
    question = request.form["question"]
    response = index.query(question, response_mode="compact")
    return f"Fish Bot says: <b>{response.response}</b>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
