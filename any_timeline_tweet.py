#extracts tweets from a user's timeline

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

trump = api.user_timeline(screen_name = 'realDonaldTrump', count = 205)  
#uses user's twitter id and twitter limits us to retrieve 200 tweets a time
for tweet in trump:
	#for text
	print "%s" % (tweet._json['text'].encode('ascii', 'ignore').decode('ascii'))
	#for json
	#print tweet
