#gives me the list of my followers on twitter

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

print "Sanjiv Pradhanang's followers on twitter: " 
print "%-25s%-25s%-25s%-25s" % ('Name', 'User ID', 'Followers', 'Location')
for follower in Cursor(api.followers).items():
	print "%-25s%-25s%-25d%-25s" % (follower._json['name'], '@'+follower._json['screen_name'], follower._json['followers_count'], follower._json['location'])
    #print json_display(follower._json)
