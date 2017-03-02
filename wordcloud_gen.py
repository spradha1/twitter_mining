#for generating a word cloud out of a text file

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'NOLA_tweetlist.txt')).read()

# read the mask image
rooster_mask = imread(path.join(d, "/home/sanjiv/Desktop/COSURP/other/roostercloud.jpg"))

wc = WordCloud(background_color="white", max_words=200, mask=rooster_mask,
               stopwords=STOPWORDS.add(""))
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "/home/sanjiv/Desktop/COSURP/other/roostercloud.jpg"))

# show
plt.imshow(wc)
plt.axis("off")
plt.imshow(rooster_mask, cmap=plt.cm.gray)
plt.show()
