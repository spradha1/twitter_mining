#authorisation of our app to access twitter through tweepy

import json
import tweepy
from tweepy import OAuthHandler #a class in tweepy
# we could have done * to import all
 
#information from twitter app
consumer_key = 'M7N7E0Wp0Mo57bYeDU5h8Zlcs'
consumer_secret = 'htS82aShch7D0eCUgDMeBQurkxH1oZGjnwD1DUUDipH11TYV6T'
access_token = '3007046359-FqGStlTSiRB2une5rHdzYzoblEnjvkdCFVtbzht'
access_secret = '81zqPgjR6BUIkAyjnzTtZvabKcafrTvV6gb5v9sFJci4q'

'''creating OAuthHandler instance
token gives access to Twitter API'''
auth = OAuthHandler(consumer_key, consumer_secret)   
auth.set_access_token(access_token, access_secret)   
 
#variable for entry point for the operations we can perform on Twitter
api = tweepy.API(auth)                  
'''dot operator used as API is not imported above  
API: wrapper for api provided with various functions'''

def process_or_store(tweet):
    print(json.dumps(tweet))
'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

for status in tweepy.Cursor(api.home_timeline).items(10):  //does the same thing as above loop in json format
    # Process a single status
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)'''

