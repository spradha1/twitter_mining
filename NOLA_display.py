"""graphs for top five hashtags and categorizing Sports, Politics, Weather, Crime tweets of New Orleans from a stream file"""
import json
import pandas as pan
import matplotlib.pyplot as plt
import re

#function for searching a word in a text
def wordf(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

#dataframe
tweets = pan.DataFrame()

#opening the data file for reading
tweets_file = open('NOLA_data.txt', 'r')

tweets_data = []
words = []
hashtags = []

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

#filling up with all the words
for t in tweets['text']:
	words1 = t.split(" ")
	for w in words1:
		words.append(w)

#finding all the hashtags
for i in words:
	hashornot = False
	if len(i)>0:
		if i[0]=='#':
			for letter in range(1,len(i)):
				ascii = ord(i[letter])
				if ascii<48 and ascii>57:
					hashornot = True
					break;
				if ascii<65 and ascii>90:
					hashornot = True
					break;
				if ascii<97 and ascii>122:
					hashornot = True
					break;
			if not hashornot:				
				hashtags.append(i)

tagtweets = pan.DataFrame({'tags':hashtags})
poptags = tagtweets['tags'].value_counts()

fig1, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=25)
ax.set_xlabel('Hashtags', fontsize=20)
ax.set_ylabel('Number of tags' , fontsize=15)
ax.set_title('Trending tags on twitter', fontsize=15, fontweight='bold')
poptags[:5].plot(ax=ax, kind='bar', color='green')
plt.grid()
plt.tight_layout() #the labels don't get clipped
fig1.savefig('Hashtags.png')

#dividing categories of tweets
tweets['Sports'] = tweets['category'].apply(lambda t: wordf('ufc', t) or wordf('football', t) or wordf('saints', t) or wordf('pelicans', t) or wordf('baseball', t) or wordf('mma', t) or wordf('basketball', t) or wordf('rousey', t) or wordf('royal rumble', t) or wordf('patriots', t))

tweets['US Politics'] = tweets['category'].apply(lambda t: wordf('trump', t) or wordf('republicans', t) or wordf('obama', t) or wordf('notmypresident', t) or wordf('white house', t) or wordf('us government', t))

tweets['Weather'] = tweets['category'].apply(lambda t: wordf('hurricane', t) or wordf('tornado', t) or wordf('storm', t) or wordf('rain', t) or wordf('hot', t) or wordf('sunny', t) or wordf('cold', t) or wordf('cloudy', t))

tweets['Crime'] = tweets['category'].apply(lambda t: wordf('drug', t) or wordf('theft', t) or wordf('murder', t) or wordf('guns', t) or wordf('shooting', t) or wordf('robbery', t) or wordf('dead', t) or wordf('police', t) or wordf('fugitive', t) or wordf('prison', t))

tweets_by_category = [tweets['Sports'].value_counts()[True], tweets['US Politics'].value_counts()[True], tweets['Weather'].value_counts()[True], tweets['Crime'].value_counts()[True]]

fig2, ax = plt.subplots()
x_pos = list(range(4))
width = 0.7
categories = ['Sports', 'US Politics', 'Weather', 'Crime']
plt.bar(x_pos, tweets_by_category, width, alpha=0.9, color='black') #plots a vertical bar graph

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=10)
ax.set_title('Tweet categories', fontsize=12, fontweight='bold')
ax.set_xticks([p + 0.5 * width for p in x_pos])
ax.set_xticklabels(categories)
plt.grid() 
fig2.savefig('NOLAcategories.png')
