#extracts data about tweets on my profile's timeline by using json keys

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

print "Data for Sanjiv Pradhanang's most recent tweets: "  
print "%-12s %-11s %-14s %-20s" % ('Tweet#', 'Likes', 'Retweets', 'Time of tweet')
for tweet in Cursor(api.user_timeline).items():
	print "%-12s %-11s %-14s %-20s" % (tweet_count, tweet._json['favorite_count'], tweet._json['retweet_count'], tweet._json['created_at'])
	tweet_count += 1
