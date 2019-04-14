import os
from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)
load_dotenv()


@app.route('/')
def main():
    return 'c4v!'


@app.route('/tweets')
def list_tweets():
    print(os.getenv('TWITTER_CONSUMER_KEY'))
    return 'All ok!'
