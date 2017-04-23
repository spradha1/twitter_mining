#function for counting number of words in a line
def num_of_words(text):
	num = 0
    #split the text
	words = text.split()
	for w in words:
		num = num + 1
	return num

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
		
#naive bayes classifier
probabilities = []
active = 0
concerned = 0
NBCpredictions = []
i_file = open('alcotweets.txt', 'r+')
all_tweets = []
label = []  
no_of_tweets = file_len('alcotweets.txt') 

#dividing tweets of each label
actives = []
concerns = []

#labeling tweets
for line in i_file: 
	all_tweets.append(line)
	if social_no(line) >= 1:
		label.append('Actively drinking')
		actives.append(line)
	else:
		label.append('Concerned about drinking')
		concerns.append(line)

for v in label:
	if(v=='Actively drinking'):
		active += 1
	else:
		concerned += 1

tweetset = [actives, concerns]
#probabilities of both labels
Pactive = active/float(no_of_tweets)
Pconcerned = concerned/float(no_of_tweets)
#number of keywords in tweets altogether & keywords belonging to specific label in each set of labeled tweets 
no_of_keywords = [0,0]


for a in actives:
	a = a.split(" ")
	for w in a:
		if(w=='alcohol' or w=='beer' or w=='wine' or w=='vodka' or w=='whiskey' or w=='liquor' or w=='drunk' or w=='intoxicated'):
			no_of_keywords[0] += 1
		
for c in concerns:
	c = c.split(" ")
	for w in c:
		if(w=='alcohol' or w=='beer' or w=='wine' or w=='vodka' or w=='whiskey' or w=='liquor' or w=='drunk' or w=='intoxicated'):
			no_of_keywords[1] += 1
			
#function for getting the probability of word being in tweets of particular label
def prob(x, n):
	num = 0
	if(x=='alcohol' or x=='beer' or x=='wine' or x=='vodka' or x=='whiskey' or x=='liquor' or x=='drunk' or x=='intoxicated'):
		for line in tweetset[n]:
			line = line.split(" ")
			for w in line:
				if(w==x):
					num += 1		
		numer = 1 + num
		denom = 8 + no_of_keywords[n]
		return numer/float(denom)
	else:
		return 1

#predict by picking category with higher probability				
for l in all_tweets:
	words = l.split(" ")
	Pa = Pactive
	Pb = Pconcerned
	for x in words:
		Pa = Pa*prob(x, 0)
		Pb = Pb*prob(x, 1)
	if(Pa>Pb):
		NBCpredictions.append('Actively drinking')
	else:
		NBCpredictions.append('Concerned about drinking')
		
#predictions display
for p in NBCpredictions:
	print p
	
#statistical analysis of the classifier	
TA = 0
TC = 0
FA = 0
FC = 0
for l,p in zip(label,NBCpredictions):
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
