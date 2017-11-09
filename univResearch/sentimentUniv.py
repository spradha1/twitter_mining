from textblob import TextBlob
import re

#function for searching a word in a text
def wordFinder(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
	
#to classify and get sentiments by popn, rank, region & followers on twitter
def update(num, line, countsCollege, sentimentsums):
	if (num==0 or num==1 or num==2 or num==4 or num==6 or num==7 or num==12 or num==15): 
		countsCollege[0] += 1
		sentimentsums[0] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[0]):
			mini[0] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[0]):
			maxi[0] = TextBlob(line).sentiment.polarity
	else:
		countsCollege[1] += 1
		sentimentsums[1] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[1]):
			mini[1] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[1]):
			maxi[1] = TextBlob(line).sentiment.polarity
		
	if (num==0 or num==1 or num==2 or num==3 or num==4 or num==5 or num==6 or num==12 or num==14 or num==15): 
		countsCollege[2] += 1
		sentimentsums[2] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[2]):
			mini[2] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[2]):
			maxi[2] = TextBlob(line).sentiment.polarity
	else:
		countsCollege[3] += 1
		sentimentsums[3] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[3]):
			mini[3] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[3]):
			maxi[3] = TextBlob(line).sentiment.polarity
		
	if (num==2 or num==5 or num==6 or num==13 or num==15): 
		countsCollege[4] += 1
		sentimentsums[4] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[4]):
			mini[4] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[4]):
			maxi[4] = TextBlob(line).sentiment.polarity
	else:
		countsCollege[5] += 1
		sentimentsums[5] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[5]):
			mini[5] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[5]):
			maxi[5] = TextBlob(line).sentiment.polarity
		
	if (num==1 or num==4 or num==6 or num==2 or num==14): 
		countsCollege[6] += 1
		sentimentsums[6] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[6]):
			mini[6] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[6]):
			maxi[6] = TextBlob(line).sentiment.polarity
	else:
		countsCollege[7] += 1
		sentimentsums[7] += TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity < mini[7]):
			mini[7] = TextBlob(line).sentiment.polarity
		if (TextBlob(line).sentiment.polarity > maxi[7]):
			maxi[7] = TextBlob(line).sentiment.polarity
		
#opening the tweet file for reading
tweets_file = open('tweetsUniv.txt', 'r')
countsCollege = [0]*8
sentimentsums = [0]*8
mini = [0]*8
maxi = [0]*8  
college = ['UNO', 'LSU', 'ULL', 'Loyola', 'Tulane', 'ULM', 'LATech', 'Delgado', 'BRCC', 'XULA', 'Dillard', 'SUNO', 'SouthEastern', 'Grambling', 'SouthernU A&M', 'Northwestern', 'Louisiana College', 'Nicholls State']
tweets_per_college = [0]*18
college_sentiment_sum = [0]*18
#going through tweets
num = 7
for line in tweets_file:
	if line: #line not empty
		if (wordFinder("@UofNO", line)):
			num = 0
		elif (wordFinder("@lsu", line)):
			num = 1
		elif (wordFinder("@ULLafayette", line)):
			num = 2
		elif (wordFinder("@Loyola_NOLA", line)):
			num = 3
		elif (wordFinder("@TulaneNews", line)):
			num = 4
		elif (wordFinder("@ULM_Official", line)):
			num = 5
		elif (wordFinder("@LATech", line)):
			num = 6
		elif (wordFinder("@delgadocc", line)):
			num = 7
		elif (wordFinder("@MyBRCC", line)):
			num = 8
		elif (wordFinder("@XULA1925", line)):
			num = 9
		elif (wordFinder("@du1869", line)):
			num = 10
		elif (wordFinder("@SUNOKnights", line)):
			num = 11
		elif (wordFinder("@oursoutheastern", line)):
			num = 12
		elif (wordFinder("@Grambling1901", line)):
			num = 13
		elif (wordFinder("@SouthernU_BR", line)):
			num = 14
		elif (wordFinder("@nsula", line)):
			num = 15
		elif (wordFinder("@LA_College", line)):
			num = 16
		elif (wordFinder("@NichollsState", line)):
			num = 17

		tweets_per_college[num] += 1
		college_sentiment_sum[num] += TextBlob(line).sentiment.polarity
		update(num, line, countsCollege, sentimentsums)
			

for t in range(0,8):
	sentimentsums[t] = sentimentsums[t]/countsCollege[t]
		
for t in range(0,18):
	college_sentiment_sum[t] = college_sentiment_sum[t]/tweets_per_college[t] 

#prints sentiment averages for different factors: popn, rank, region, followers on twitter
'''for s,c,l,h in zip (sentimentsums, countsCollege, mini, maxi):
	print ('%.3f %d' + str(l).rjust(5) + str(h).rjust(5)) % (s, c)'''
	
print 'College'.rjust(25) + 'No. of tweets'.rjust(15) + 'Average sentiment score'.rjust(30)
for n,t,s in zip(college, tweets_per_college, college_sentiment_sum):
	print n.rjust(25) + str(t).rjust(15) + str(s).rjust(30)
