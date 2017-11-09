#Naive bayes classifier

from catLabel2 import *

predictions = []
predictions1 = []
label1 = []
trainfile = open('sampleharvey.txt', 'r+')
testfile = open('tweetsUniv.txt', 'r+')
train_tweets = []
test_tweets = []
relevant_tweets = []
no_of_tweets = 1239

#separating tweet lists
harveytweets = []
schooltweets = []
irrelevanttweets = []
totalwords = [0, 0, 0]

for t in testfile:
	test_tweets.append(t)

for l,t in zip(train2, trainfile):
	train_tweets.append(t)
	if (l=='h'):
		harveytweets.append(t)
	elif (l=='e'):
		schooltweets.append(t)
	else:
		irrelevanttweets.append(t)

for ht in harveytweets:
	htw = ht.split(" ")
	totalwords[0] += len(htw)

for st in schooltweets:
	stw = st.split(" ")
	totalwords[1] += len(stw)

for it in schooltweets:
	itw = it.split(" ")
	totalwords[2] += len(itw)

tweetset = [harveytweets, schooltweets, irrelevanttweets]

#probabilities of a tweet being of a specific category
harveyn = 0
schooln = 0
irrelevantn = 0

for tag in train2:
	if(tag=='h'):
		harveyn += 1
	elif(tag=='e'):
		schooln += 1
	else:
		irrelevantn += 1

Phar = harveyn/float(no_of_tweets)
Psch = schooln/float(no_of_tweets)
Pirr = irrelevantn/float(no_of_tweets)

#function for getting the probability of word being in tweets of particular label
def prob(x, n):
	num = 0
	for tline in tweetset[n]:
		tline = tline.split(" ")
		for w in tline:
			if(w.lower()==x.lower()):
				num += 1
	numer = 1 + num
	denom = 2657 + totalwords[n]
	return numer/float(denom)

#predict by picking category with higher probability
for l in test_tweets:
	words = l.split(" ")
	Ph = Phar
	Ps = Psch
	Pi = Pirr
	for x in words:
		Ph = Ph*prob(x, 0)
		Ps = Ps*prob(x, 1)
		Pi = Pi*prob(x, 2)
	if(Ph>Ps and Ph>Pi):
		predictions.append('h')
	elif(Ps>Ph and Ps>Pi):
		predictions.append('e')
	else:
		predictions.append('i')

#predictions display
'''for p in predictions:
	print p'''

#statistical analysis of the classifier
#relevant vs. irrelevant
Trev = 0
Tirr = 0
Frev = 0
Firr = 0
for l,p in zip(label2, predictions):
	if(l=='i' and l==p):
		Tirr += 1
	elif((l=='h' or l=='e') and l==p):
		Trev += 1
		label1.append(l)
		predictions1.append(p)
	elif((l=='h' or l=='e') and l!=p):
		Firr += 1
		label1.append(l)
		predictions1.append(p)
	elif(l=='i' and l!=p):
		Frev += 1

precisionRev = Trev/float(Trev+Frev)
recallRev = Trev/float(Trev+Firr)
precisionIrr = Tirr/float(Tirr+Firr)
recallIrr = Tirr/float(Tirr+Frev)
F1rev = 2*(precisionRev*recallRev)/(precisionRev+recallRev)
F1irr = 2*(precisionIrr*recallIrr)/(precisionIrr+recallIrr)
accuracy = (Trev+Tirr)/float(Trev+Tirr+Frev+Firr)

print ('Relevant: Precision: %.4f Recall: %.4f F1 score: %.4f') % (precisionRev, recallRev, F1rev)
print ('Irrelevant: Precision: %.4f Recall: %.4f F1 score: %.4f') % (precisionIrr, recallIrr, F1irr)
print ('Accuracy: %.4f') % (accuracy)

#harvey vs. school experience(non-harvey)

#getting only the relevant tweets
for l,t in zip(label2, test_tweets):
	if(l=='h' or l=='e'):
		relevant_tweets.append(t)

Thar = 0
Tsch = 0
Fhar = 0
Fsch = 0
for l,p in zip(label1, predictions1):
	if(l=='h' and l==p):
		Thar += 1
	elif(l=='e' and l==p):
		Tsch += 1
	elif(l=='e' and l!=p):
		Fhar += 1
	elif(l=='h' and l!=p):
		Fsch += 1

precisionHar = Thar/float(Thar+Fhar)
recallHar = Thar/float(Thar+Fsch)
precisionSch = Tsch/float(Tsch+Fsch)
recallSch = Tsch/float(Tsch+Fhar)
F1har = 2*(precisionHar*recallHar)/(precisionHar+recallHar)
F1sch = 2*(precisionSch*recallSch)/(precisionSch+recallSch)
accuracy1 = (Thar+Tsch)/float(Thar+Tsch+Fhar+Fsch)
print ('Harvey: Precision: %.4f Recall: %.4f F1 score: %.4f') % (precisionHar, recallHar, F1har)
print ('School Experience: Precision: %.4f Recall: %.4f F1 score: %.4f') % (precisionSch, recallSch, F1sch)
print ('Accuracy: %.4f') % (accuracy1)
