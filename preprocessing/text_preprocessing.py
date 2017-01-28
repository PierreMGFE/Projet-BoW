from preprocessing.load_files import data
import nltk
from re import sub
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
import time

stops = set(nltk.corpus.stopwords.words("english"))

stemmer = SnowballStemmer("english", ignore_stopwords=True)
lemmatizer = WordNetLemmatizer()
porter = PorterStemmer()
lancaster = LancasterStemmer()

# TODO : virer toutes les mots qui n'ont que des majuscules
clean_data = data

for year in data.keys():
    for country, report in data[year].items():
        letters_only = sub("[^a-zA-Z]", " ", report)
        words = letters_only.lower().split()
        meaningful_words = [w for w in words if w not in stops]
        #stemmed_words = [porter.stem(w) for w in meaningful_words]
        stemmed_words = meaningful_words
        clean_data[year][country] = ' '.join(stemmed_words)




# nltk_lw_2_NotDigit = sorted([item for item in nltk_lw_2 if not item.isdigit()])
# nltk_lw_2_AlphaBet = sorted([item for item in nltk_lw_2 if item.isalpha()])
# nltk_lw_2_AlphaBet_lower = sorted([item.lower() for item in nltk_lw_2_AlphaBet])
#
#
# #definition des stopwords
# stop = set(nltk.corpus.stopwords.words('english'))
# nltk_lw_2_AB_WOstop = sorted([item.lower() for item in nltk_lw_2 if item.isalpha() and item not in stop])
#
# fq_lw_2 = nltk.FreqDist(nltk_lw_2_AB_WOstop)
#
# fq_lw_2.plot(50, cumulative=True)