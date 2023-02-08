import functions_framework
from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

@functions_framework.http
def hello_http(request):
   """HTTP Cloud Function.
   Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
   Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
   """
   request_json = request.get_json(silent=True)
   request_args = request.args

   if request_json and 'name' in request_json:
       name = request_json['name']
   elif request_args and 'name' in request_args:
       name = request_args['name']
   else:
       name = 'World'
   return 'Hello {}!'.format(name)

def ask_fish():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("What do you want to ask Fish? ")
        response = index.query(query, response_mode="compact", verbose=False)
        display(Markdown(f"Fish Bot says: <b>{response.response}</b>"))
