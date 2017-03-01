"""Naive Bayes Classifier for text file to classify into world topics, yet to be fixed for unclassfied data"""
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
	if(q==0):
		for w in category_word_packets[q]:
			if not (w=='superbowl' or w=='ball' or w=='champions' or w=="baseball" or w=='wwe' or w=='basketball' or w=='sports' or w=='falcons' or w=='patriots' or w=='brady' or w=='score' or w=='win' or w=='loss' or w=='photo' or w=='hollywood' or w=='bollywood' or w=='movie' or w=='album' or w=='song' or w=='film' or w=='rap' or w=='music' or w=='acting' or w=='fake' or w=="drama" or w=='world' or w=='hurricane' or w=='tornado' or w=='storm' or w=='rain' or w=='hot' or w=='sun' or w=='cold' or w=='cloudy' or w=='job' or w=='showers' or w=='wind' or w=='snow' or w=='temperature' or w=='fog' or w=='trump' or w=='clinton' or w=='border' or w=='government' or w=='law' or w=='parliament' or w=='donald' or w=='ban' or w=='president' or w=='minister' or w=='election' or w=='tax' or w=='cost' or w=='country' or w=='phone' or w=='call' or w=='android' or w=='science' or w=='cure' or w=='app' or w=='system' or w=='apple' or w=='computer' or w=='mac' or w=='windows' or w=='cancer' or w=='time' or w=='moon' or w=='eclipse' or w=='research' or w=='college' or w=='university' or w=='institute' or w=='machine' or w=='course'):
				num += 1
	else:
		for worrd in category_word_packets[q]:
			if(y==worrd):
				num += 1
	count = num + 1
	denom = 6247 + totalwords[q]
	return (float(count)/denom)


#dataframe
tweets = pan.DataFrame()

#opening the data file for reading
tweets_file = open('naiveStream.txt', 'r')

tweets_data = []
classcount = [0, 0, 0, 0]
classnames = ["Unclassified", "Sports & Entertainment", "News", "Science & Technology"]

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
tweets['category'] = map(lambda tweet: tweet['text'].lower(), tweets_data)

#total number of words in each category of tweets
totalwords = [0, 0, 0, 0]
#words in each type of tweet
category_word_packets = [[],[],[],[]]
#classifying every tweet
for t in tweets['category']:
	words1 = t.split(" ")
	words = 0
	#categories tweet counter
	classes = [0, 0, 0, 0]
	for w in words1:
		if(w=='superbowl' or w=='ball' or w=='champions' or w=="baseball" or w=='wwe' or w=='basketball' or w=='sports' or w=='falcons' or w=='patriots' or w=='brady' or w=='score' or w=='win' or w=='loss' or w=='photo' or w=='hollywood' or w=='bollywood' or w=='movie' or w=='album' or w=='song' or w=='film' or w=='rap' or w=='music' or w=='acting' or w=='fake' or w=="drama" or w=='world'):
			classes[1] += 1
		elif(w=='hurricane' or w=='tornado' or w=='storm' or w=='rain' or w=='hot' or w=='sun' or w=='cold' or w=='cloudy' or w=='job' or w=='showers' or w=='wind' or w=='snow' or w=='temperature' or w=='fog' or w=='trump' or w=='clinton' or w=='border' or w=='government' or w=='law' or w=='parliament' or w=='donald' or w=='ban' or w=='president' or w=='minister' or w=='election' or w=='tax' or w=='cost' or w=='country'):
			classes[2] += 1
		elif(w=='phone' or w=='call' or w=='android' or w=='science' or w=='cure' or w=='app' or w=='system' or w=='apple' or w=='computer' or w=='mac' or w=='windows' or w=='cancer' or w=='time' or w=='moon' or w=='eclipse' or w=='research' or w=='college' or w=='university' or w=='institute' or w=='machine' or w=='course'):
			classes[3] += 1
		words += 1
	maxclass = classifier(classes)
	classcount[maxclass] += 1
	totalwords[maxclass] += words   #adding number of words in tweet after classification
	for w in words1:
		category_word_packets[maxclass].append(w)

#displaying stats for the tweet file
for r in range(0,4):
	print "%s: %d" % (classnames[r], classcount[r])

input_tweet = raw_input("Enter your tweet: ")
x = input_tweet.lower().split(" ")
probs = [0, 0, 0, 0]   #probabilities by category

#calculating probability
for q in range(0,4):
	prob = classcount[q]/1655.0
	for y in x:
		prob = prob*est(y,q)
	probs[q] = prob

#displaying probabilities
for k in range(0,4):
	print "%s: %.25f" % (classnames[k], probs[k])
