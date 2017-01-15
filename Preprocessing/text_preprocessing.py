from Preprocessing.load_files import data
import nltk
from re import sub

stops = set(nltk.corpus.stopwords.words("english"))

# Simple cleaning (cf Kaggle tutorial)

clean_data = []
for year in data.keys():
    for country, report in data[year].items():
        letters_only = sub("[^a-zA-Z]", " ", report)
        words = letters_only.lower().split()
        meaningful_words = [w for w in words if w not in stops]
        clean_data.append(" ".join(meaningful_words))

