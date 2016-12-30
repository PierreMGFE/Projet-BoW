import os

import nltk

lw_2 = list_file(path)
nltk_lw_2 = nltk.Text(lw_2)


nltk_lw_2_NotDigit = sorted([item for item in nltk_lw_2 if not item.isdigit()])
nltk_lw_2_AlphaBet = sorted([item for item in nltk_lw_2 if item.isalpha()])
nltk_lw_2_AlphaBet_lower = sorted([item.lower() for item in nltk_lw_2_AlphaBet])


#definition des stopwords
stop = set(nltk.corpus.stopwords.words('english'))
nltk_lw_2_AB_WOstop = sorted([item.lower() for item in nltk_lw_2 if item.isalpha() and item not in stop])

fq_lw_2 = nltk.FreqDist(nltk_lw_2_AB_WOstop)

fq_lw_2.plot(50, cumulative=True)


