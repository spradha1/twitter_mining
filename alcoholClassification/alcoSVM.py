from sklearn import svm, preprocessing
import numpy as np
import re

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
   
#function for computing the fraction of keywords in a line
def w_fraction(text):
	num = 0 
	keys = ['alcohol', 'beer', 'wine', 'vodka', 'whiskey', 'liquor', 'drunk', 'intoxicated']
	words = text.split()
	for w in words:
		for k in keys:
			if k==w.lower():
				num = num + 1.0
	return num/num_of_words(text)

#function for returning number of words in a line indicating actively drunk user 		
def social_no(text):
	num = 0 
	keys = ['drunk', 'intoxicated']
	words = text.split()
	for w in words:
		for k in keys:
			if k==w.lower():
				num = num + 1
	return num 


i_file = open('alcotweets.txt', 'r+')
pureTweets = []
label = []  
no_of_tweets = file_len('alcotweets.txt') 

#labeling tweets
for line in i_file:
	pureTweets.append([num_of_words(line), w_fraction(line), social_no(line)]) 
	if social_no(line) >= 1:
		label.append('Actively drinking')
	else:
		label.append('Concerned about drinking')

#printing out labels
for j in label:
	print j
		
#SVM classifier	
pureTweets = (preprocessing.MaxAbsScaler()).fit_transform(np.array(pureTweets)) 
classifier = svm.SVC(kernel = 'linear', C =1.0)
classifier.fit(pureTweets,label)
SVMpredictions = []

for t in pureTweets:
	SVMpredictions.append(str(classifier.predict(t))[2:-2])
#predictions display
for p in SVMpredictions:
	print p
#statistical analysis of the classifier
TA = 0
TC = 0
FA = 0
FC = 0
for l,p in zip(label,SVMpredictions):
	if(l=='Actively drinking' and l==p):
		TA += 1
	elif(l=='Concerned about drinking' and l==p):
		TC += 1
	elif(l=='Concerned about drinking' and l!=p):
		FA += 1
	elif(l=='Actively drinking' and l!=p):
		FC += 1

precisionA = TA/float(TA+FA)
recallA = TA/float(TA+FC)
precisionC = TC/float(TC+FC)
recallC = TC/float(TC+FA)
F1A = 2*(precisionA*recallA)/(precisionA+recallA)
F1C = 2*(precisionC*recallC)/(precisionC+recallC)
acc = (TA+TC)/float(TA+TC+FA+FC)

print ('Actively drinking: Precision: %.4f Recall: %.4f F1 score: %.4f') % (precisionA, recallA, F1A)
print ('Concerned about drinking: Precision: %.4f Recall: %.4f F1 score: %.4f') % (precisionC, recallC, F1C)
print ('Accuracy: %.4f') % (acc)
