#Retrieves tweets from a region roughly in json using location filter

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3007046359-FqGStlTSiRB2une5rHdzYzoblEnjvkdCFVtbzht"
access_token_secret = "81zqPgjR6BUIkAyjnzTtZvabKcafrTvV6gb5v9sFJci4q"
consumer_key = "M7N7E0Wp0Mo57bYeDU5h8Zlcs"
consumer_secret = "htS82aShch7D0eCUgDMeBQurkxH1oZGjnwD1DUUDipH11TYV6T"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by location coordinates of New Orleans(around 37N, 90W)
    stream.filter(locations=[-116.25,31,-70,50])
