#displays data in graphs for language, country and [python, js, ruby] from a stream file of tweets

import json
import pandas
import matplotlib.pyplot as plt
import re

#function for searching a word in a text
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets_data_path = 'twitter_data.txt'
tweets_data = []

#opening the data file for reading
tweets_file = open(tweets_data_path, "r")
#load each tweet into a list
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print "Tweets retrieved: %d" % (len(tweets_data))

tweets = pandas.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

fig1, ax = plt.subplots() #returns a tuple of a figure & axes objects
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
plt.grid() #grid on for graph
plt.tight_layout()
fig1.savefig('Language_graph.png')

tweets_by_country = tweets['country'].value_counts()

fig2, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
plt.grid()
plt.tight_layout() #the labels don't get clipped
fig2.savefig('Country_graph.png')

tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

print "Number of tweets with 'python': %d" % (tweets['python'].value_counts()[True])
print "Number of tweets with 'javascript': %d" % (tweets['javascript'].value_counts()[True])
print "Number of tweets with 'ruby': %d" % (tweets['ruby'].value_counts()[True])

prg_langs = ['python', 'javascript', 'ruby']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.7
fig3, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=0.7, color='m') #plots a vertical bar graph

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=1)
ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=13, fontweight='bold')
ax.set_xticks([p + 0.5 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid() 
fig3.savefig('Prog_lang_graph.png')

#now only considering relevant tweets
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
print "Relevant tweets retrieved: %d (with the word 'programming')" % (tweets['relevant'].value_counts()[True])

print "Number of tweets with 'python': %d" % (tweets[tweets['relevant'] == True]['python'].value_counts()[True])
print "Number of tweets with 'javascript': %d" % (tweets[tweets['relevant'] == True]['javascript'].value_counts()[True])
print "Number of tweets with 'ruby': %d" % (tweets[tweets['relevant'] == True]['ruby'].value_counts()[True])

tweets_by_relevant_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], tweets[tweets['relevant'] == True]['javascript'].value_counts()[True], tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]]

fig4, ax = plt.subplots()
plt.bar(x_pos, tweets_by_relevant_prg_lang, width, alpha=0.7, color='y') #plots a vertical bar graph

# Setting axis labels and ticks
ax.set_ylabel('Number of relevant tweets', fontsize=1)
ax.set_title('Ranking: python vs. javascript vs. ruby (Raw relevant data)', fontsize=12, fontweight='bold')
ax.set_xticks([p + 0.5 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid() 
fig4.savefig('Relevant_Prog_lang_graph.png')
