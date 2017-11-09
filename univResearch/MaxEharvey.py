#Maximum Entropy Classifier

from nltk.classify import maxent
import numpy as np
import re
from textblob import TextBlob
from catLabel2 import *

#function for counting number of words in a line
def num_of_words(text):
	num = 0
    #split the text
	words = text.split()
	for w in words:
		num = num + 1
	return num

#function for searching a word in a text
def wordf(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

#function for computing the number of lines in a file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#function for computing the number of http's in a line
def http(text):
	num = 0
	words = text.split()
	for w in words:
		if w[0:4] == 'http':
			num = num + 1
	return num

#function for computing the number of the words beginning with "class" in a line
def harvey(text):
	num = 0
	words = text.split()
	for w in words:
		if w.lower()[0:5] == 'class' or w.lower()[0:6] == 'harvey' or w.lower()[0:6] == 'cancel':
			num = num + 1
	return num

#function for returning number of twitter handles in a line
def handle(text):
	num = 0
	words = text.split()
	for w in words:
		if w[0] == '@':
			num = num + 1
	return num

trainfile = open('sampleharvey.txt', 'r+')
testfile = open('tweetsUniv.txt', 'r+')

train = []
test = []

for t,l in zip(trainfile, train2):
	train.append(({'words':num_of_words(t), 'https':http(t), 'harveyWords': harvey(t), 'handles': handle(t), 'sentiment':TextBlob(t).sentiment.polarity}, l))

for t in testfile:
	test.append({'words':num_of_words(t), 'https':http(t), 'harveyWords':harvey(t), 'handles': handle(t), 'sentiment':TextBlob(t).sentiment.polarity}) 

encoding = maxent.TypedMaxentFeatureEncoding.train(train, count_cutoff=5, alwayson_features=True)
classifier = maxent.MaxentClassifier.train(train, bernoulli=False, encoding=encoding, trace=0)
MEpredictions = classifier.classify_many(test)

MEpredictions1 = []
label1 = []

Trev = 0
Tirr = 0
Frev = 0
Firr = 0
for l,p in zip(label2, MEpredictions):
	if(l=='i' and l==p):
		Tirr += 1
	elif((l=='h' or l=='e') and l==p):
		Trev += 1
		label1.append(l)
		MEpredictions1.append(p)
	elif((l=='h' or l=='e') and l!=p):
		Firr += 1
		label1.append(l)
		MEpredictions1.append(p)
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

Thar = 0
Tsch = 0
Fhar = 0
Fsch = 0
for l,p in zip(label1, MEpredictions1):
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
