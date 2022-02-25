# Read in the document-term matrix
import pandas as pd

data = pd.read_pickle('dtm_m.pkl')
data = data.transpose()

# Find the top 30 words in each movie srcipt
top_dict = {}
for c in data.columns:
    top = data[c].sort_values(ascending=False).head(30)
    top_dict[c]= list(zip(top.index, top.values))
    
# Look at the most common top words --> add them to the stop word list
from collections import Counter

# Let's first pull out the top 30 words for each movie
words = []
for movies in data.columns:
    top = [word for (word, count) in top_dict[movies]]
    for t in top:
        words.append(t)  

# Let's aggregate this list and identify the most common words along with how many routines they occur in
#print(Counter(words).most_common())

# If more than three of the movies have it as a top word, exclude it from the list
add_stop_words = [word for word, count in Counter(words).most_common() if count >=4]

# Add characters' names to stopword list
character_names = ['mia','miarn','sebastian','sebastianrn','celinern','jessern','jake','jakern','rnjake',
                   'neytiri','rnthe','josh','morpheus','morpheusrn','thern','neorn','renai','rna',
                   'gracern','grace','travis','dalton','beverly','ben','richie','benrn','eddiern','beverlyrn',
                   'richiern','eddie','rnhe','contd','elise','billrn','ethan','rnethan','nyah','swanbeck','luther',
                   'billy','ambrose','bourne','hes','bournern','marie','mariern']
add_stop_words.extend(character_names)

#update our document-term matrix with the new list of stop words
from sklearn.feature_extraction import text 
from sklearn.feature_extraction.text import CountVectorizer

# Read in cleaned data
data_clean = pd.read_pickle('data_clean_m.pkl')

# Add new stop words
stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)

# present the result by word clouds!
from wordcloud import WordCloud

wc = WordCloud(stopwords=stop_words, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)

# Reset the output dimensions
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16, 6]
movies_full = ['LA LA Land','Before Sunrise','The Matrix','Avatar','Insidious','It','Mission Impossible 2','The Bourne Identity']

# Create subplots for each comedian
for index, movies in enumerate(data.columns):
    wc.generate(data_clean.script[movies])
    
    plt.subplot(3, 4, index+1)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(movies_full[index])
    
plt.show()