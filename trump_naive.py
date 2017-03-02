#naive bayes classifier for sentiments on trump's tweets from a the text file of tweets(not a stream file), not fixed for unclassified tweets
import json
import pandas as pan
from math import *

#finds index of the max value in the list
def classifier(classes):
	maxwords = 0
	iclass = 0
	for n in range(0, len(classes)):
		if(classes[n]>maxwords):
			maxwords=classes[n]
			iclass = n
	return iclass

#uses the formula (count+1)/(total words in category + total unique words)
def est(y, q):
	num = 0
	'''if(q==0):
		for w in category_word_packets[q]:
			if not (w=='illegal' or w=='wall' or w=='build' or w=='democrats' or w=='mexico' or w=='obama' or w=='russia' or w=='ban' or w=='border' or w=='iran' or w=='job' or w=='security' or w=='fake' or w=='failing' or w=='failure' or w=='travel' or w=='country' or w=='legal' or w=='bad' or w=='deal' or w=='happy' or w=='U.S.' or w=='united' or w=='states' or w=='national' or w=='safety' or w=='trump' or w=='president' or w=='election' or w=='won' or w=='great' or w=='good' or w=='ivanka' or w=='make' or w=='america' or w=='again' or w=='people' or w=='law' or w=='power' or w=='donald' or w=='right'):
				num += 1
	else:'''
	for worrd in category_word_packets[q]:
		if(y==worrd):
			num += 1
	count = num + 1
	denom = 1621 + totalwords[q]
	return (float(count)/denom)

#opening the tweet text file
f = open('trump_tweets.txt', 'r')
tweetarray = []
for ti in f:
	tweetarray.append(ti)

''' this section of code didn't work for some reason 
#dataframe
tweets = pan.DataFrame()

#opening the data file for reading
tweets_file = open('trump_stream.txt', 'r')
tweets_data = []

#load each tweet into a list
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#list of text of tweets
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#lower case version for looking up words so that case doesn't matter
tweets['categories'] = map(lambda tweet: tweet['text'].lower(), tweets_data)'''

sentiment_count = [0, 0, 0]
sentiment_names = ["Unclassified", "Angry", "Happy"]
#total number of words in each category of tweets
totalwords = [0, 0, 0]
#words in each type of tweet
category_word_packets = [[],[],[]]
#classifying every tweet
for l in tweetarray:
	words1 = l.split(" ")
	words = 0
	#categories tweet counter
	sentiments = [0, 0, 0]
	for w in words1:
		if(w=='illegal' or w=='wall' or w=='build' or w=='democrats' or w=='mexico' or w=='obama' or w=='russia' or w=='ban' or w=='border' or w=='iran' or w=='job' or w=='security' or w=='fake' or w=='failing' or w=='failure' or w=='travel' or w=='country' or w=='legal' or w=='bad' or w=='deal'):
			sentiments[1] += 1
		elif(w=='happy' or w=='U.S.' or w=='united' or w=='states' or w=='national' or w=='safety' or w=='trump' or w=='president' or w=='election' or w=='won' or w=='great' or w=='good' or w=='ivanka' or w=='make' or w=='america' or w=='again' or w=='people' or w=='law' or w=='power' or w=='donald' or w=='right'):
			sentiments[2] += 1
		words += 1
	maxclass = classifier(sentiments)
	sentiment_count[maxclass] += 1
	totalwords[maxclass] += words   #adding number of words in tweet after classification
	for w in words1:
		category_word_packets[maxclass].append(w)

#displaying stats for the tweet file
for r in range(0,3):
	print "%s: %d" % (sentiment_names[r], sentiment_count[r])

input_tweet = raw_input("Enter your tweet: ")
x = input_tweet.lower().split(" ")
probs = [0, 0, 0]   #probabilities by category

#calculating probability
for q in range(0,3):
	prob = sentiment_count[q]/215.0
	for y in x:
		prob = prob*est(y,q)
	probs[q] = prob

#displaying probabilities
for k in range(0,3):
	print "%s: %.20f" % (sentiment_names[k], probs[k])
