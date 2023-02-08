import sys
import os
import openai

from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI


from IPython.display import Markdown, display
from flask import Flask

app = Flask(__name__)



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
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    question = request.form["question"]
    response = index.query(query, response_mode="compact", verbose=False)
    
    display(Markdown(f"Fish Bot says: <b>{response.response}</b>"))
    return f"Fish Bot says: <b>{response.response}</b>"


def ask_fish():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("What do you want to ask Fish? ")
        response = index.query(query, response_mode="compact", verbose=False)
        display(Markdown(f"Fish Bot says: <b>{response.response}</b>"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
