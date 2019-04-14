import os
import twitter
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def main():
    return 'c4v!'


@app.route('/tweets')
def list_tweets():
    api = twitter.Api(
        consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
        consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
        access_token_key=os.getenv('TWITTER_ACCESS_TOKEN_KEY'),
        access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )

    tweets_list = api.GetSearch(raw_query='q=sinluz&count=5')

    result = {}
    for tweet in tweets_list:
        result[tweet.id] = tweet.text

    return jsonify(result)
