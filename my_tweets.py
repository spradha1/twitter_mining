#extracts my recent tweets

import json
from tweepy import *

#connection to twitter app
consumer_key = 'M7N7E0Wp0Mo57bYeDU5h8Zlcs'
consumer_secret = 'htS82aShch7D0eCUgDMeBQurkxH1oZGjnwD1DUUDipH11TYV6T'
access_token = '3007046359-FqGStlTSiRB2une5rHdzYzoblEnjvkdCFVtbzht'
access_secret = '81zqPgjR6BUIkAyjnzTtZvabKcafrTvV6gb5v9sFJci4q'

auth = OAuthHandler(consumer_key, consumer_secret)   
auth.set_access_token(access_token, access_secret) 

api = API(auth)

#function to display in json format
def json_display(tweet):
    print(json.dumps(tweet))

tweet_count = 1

print "Sanjiv Pradhanang's recent tweets: "

for tweet in Cursor(api.user_timeline).items():
	print "%d. %s" % (tweet_count, tweet._json['text'])
	tweet_count+=1
