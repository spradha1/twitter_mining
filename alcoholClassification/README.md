Sanjiv Pradhanang 04/23/2017

These files are related to a task of constructing simple classifiers: SVM with linear kernel and Naive Bayes Classifier. The tweets were streamed using word filters related to drinking. Tweets from all around the world were streamed at April 20, 2017 21:01:17 CT for a few minutes. That was enough to get 631 tweets with the words chosen. Due to time and resource limitations, larger amount of data was not used. A rough classification was done into categories "Concerned about drinking" and "Actively drinking". 

On basis of certain words present in the tweets, the classification was done. The "Actively drinking" category seemed to have really low number and thus the program was modified to label more tweets for that category by simply assuming that tweets having words "drunk" and "intoxicated" fell in that category regardless of how much of the other category's contents lied in those tweets. The categories were thus decided to somewhat estimate the number of tweets coming from actively drunk people and people who just like to talk on the topic of drinking.

The same tweets were then classified by the classifiers. SVM used fields: number of words in tweet, number of words in "Actively drinking" category, and fraction of alcohol-related words in the tweet in order to classify the tweets.
Naive Bayes Classifier basically looked at only the alcohol-related words and combined the probability of each of those words in a tweet to calculate the overall probabilities of the tweets to fall in each category. The category with higher probability was chosen.

SVM seemed to be the better classifier predicting all the 631 labels correctly. 
