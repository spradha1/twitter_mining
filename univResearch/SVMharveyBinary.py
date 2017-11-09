'''SVM: taking a one vs. all approach (prefered)
first classifying as relevant & irrelevant
& then classifying the relevant data into Harvey-related and school-related'''

﻿from sklearn import svm, preprocessing
import numpy as np
import re
from textblob import TextBlob
from catLabel1 import *
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

#function for computing the number of the words beginning with harvey-related words in a line
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
data_train = []
data_test = []

#data for tweets
for line in trainfile:
	data_train.append(np.array([num_of_words(line), http(line), handle(line), harvey(line), TextBlob(line).sentiment.polarity]))

for line in testfile:
	data_test.append(np.array([num_of_words(line), http(line), handle(line), harvey(line), TextBlob(line).sentiment.polarity]))

#SVM classifier
#data_of_tweets = (preprocessing.MaxAbsScaler()).fit_transform(np.array(data_of_tweets))
classifier1 = svm.SVC(kernel='rbf', C=1.0)
classifier1.fit(data_train, train1)
SVMpredictions = []

for t in data_test:
	SVMpredictions.append(classifier1.predict(t))
	
#predictions display
'''for p in SVMpredictions:
	print p'''
	
SVMpredictions1 = []
onelabel = []
train3 = []
data_train_again = []
data_test_again = []

Trev = 0
Tirr = 0
Frev = 0
Firr = 0
for l,p,n,t in zip(label1, SVMpredictions, label2, data_test):
	if(l=='i' and l==p):
		Tirr += 1
	elif((l=='r') and l==p):
		Trev += 1
		onelabel.append(n)
		data_test_again.append(t)
	elif((l=='r') and l!=p):
		Firr += 1
		onelabel.append(n)
		data_test_again.append(t)
	elif(l=='i' and l!=p):
		Frev += 1

#taking 900 tweets out of the relevant ones for training for the second classification
for x in range(0, 900):
	data_train_again.append(data_test_again[x])
	train3.append(onelabel[x])

#preparing classifier for the second classification task
classifier2 = svm.SVC(kernel='rbf', C=1.0)
classifier2.fit(data_train_again, train3)

for t in data_test_again:
	SVMpredictions1.append(classifier2.predict(t))      #predictions for relevant tweets
	
#classification 1	
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
for l,p in zip(onelabel, SVMpredictions1):
	if(l=='h' and l==p):
		Thar += 1
	elif(l=='e' and l==p):
		Tsch += 1
	elif(l=='e' and l!=p):
		Fhar += 1
	elif(l=='h' and l!=p):
		Fsch += 1

#classification 2
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

#for calculating number of tweets in each category
'''h=0
e=0
i=0
for t in label:
	if (t=='h'):
		h+=1
	elif (t=='e'):
		e+=1
	else:
		i+=1
print h, e, i'''
