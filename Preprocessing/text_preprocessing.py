from Preprocessing.load_files import data
import nltk
from re import sub

stops = set(nltk.corpus.stopwords.words("english"))

# Simple cleaning (cf Kaggle tutorial)

clean_data = dict()
for year in data.keys():
    clean_data[year] = dict()
    for country, report in data[year].items():
        letters_only = sub("[^a-zA-Z]", " ", report)
        words = letters_only.lower().split()
        meaningful_words = [w for w in words if w not in stops]
        clean_data[year][country] = " ".join(meaningful_words)


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