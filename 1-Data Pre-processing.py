# movie names
movies = ['LA LA Land','Before Sunrise','The Matrix','Avatar','Insidious','It','Mission Impossible 2','The Bourne Identity']

# Read txt files
data = {}
for i, c in enumerate(movies):
    with open("scripts\\" + c +".txt", "rb") as file:
        data[c] = file.read()

# change this to key: movie, value: string format
def combine_text(list_of_text):
    '''Takes a list of text and combines them into one large chunk of text.'''
    combined_text = ''.join(str(list_of_text))
    return combined_text
    
# Combine it!
data_combined = {key: [combine_text(value)] for (key, value) in data.items()}

# put it into a pandas dataframe
import pandas as pd
pd.set_option('max_colwidth',150)
data_df = pd.DataFrame.from_dict(data_combined).transpose()
data_df.columns = ['script']

# Apply text cleaning techniques
import re
import string

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

round1 = lambda x: clean_text_round1(x)

# the updated text
data_clean = pd.DataFrame(data_df.script.apply(round1))

# add the movie names to the dataframe
data_clean['movie names'] = movies

# create a document-term matrix using CountVectorizer, and exclude common English stop words
from sklearn.feature_extraction.text import CountVectorizer
import pickle

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.script)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names_out())
data_dtm.index = data_clean.index

# pickle it for later use
data_dtm.to_pickle("dtm_m.pkl")

# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
data_clean.to_pickle('data_clean_m.pkl')
pickle.dump(cv, open("cv_m.pkl", "wb"))

