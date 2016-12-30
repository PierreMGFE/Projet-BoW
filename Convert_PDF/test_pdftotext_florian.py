import os

import nltk
from settings import ROOT_DIR


def list_file(name_file):
    """
    Return a list of all words in a file
    :param name_file : string -> path towards the file
    :return: list -> contains all words in file
    """
    with open(name_file, "r") as file:
        list_words = file.read().split()
    return list_words


dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(dir_path)

country = "Afghanistan"
path = os.path.join(ROOT_DIR, "/text_data/pdftotext/SCD/2016/SCD_{0}_2016.txt".format(country))
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


