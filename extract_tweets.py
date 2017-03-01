#extracts tweets' text from a stream file 

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

#opening the data file for reading
tweets_file = open('naiveStream.txt', 'r')
tweets_data = []

for line in tweets_file:
    try:
        l = json.loads(line)
        tweets_data.append(l)
    except:
        continue

for tweet in tweets_data:
	print tweet['text'].encode('ascii', 'ignore').decode('ascii') #clearing out Unicode error for characters not in the 128 range of ascii characters
