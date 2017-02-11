from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from preprocessing.load_files import data
import re

stop_words = list(stopwords.words('english'))


class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in wordpunct_tokenize(doc) if t.isalpha()]


spec_words = ["pdf", "imagebank", "servlet", "wdscontentserver", 'aaa', 'access', 'also',
              'achieved', 'ida', 'ifc', 'ii', 'ta', 'wbg', 'us']
econ_words = ["sector", "percent", "figure", "country", "bank", 'cps', 'development', 'government',
              'management', 'program', 'project', 'public', 'services', 'support']
country_words = ["botswana", "lesotho", "sudan", "uganda", "mali", "côte", "ivoire", "chad", "brazil", "serbia",
                 "haiti", "bolivia", "tunisia", "bangladesh", "panama", "colombia", "honduras", "costa", "rica",
                 "sri", "lanka", "lebanon", "mauritius", "egypt", "uruguay", "maldives"]
country_words = list(country_words)+["sri", "lanka", "côte", "ivoire", "costa", "rica", "bosnia", "herzegovina"]
banned_words = spec_words + econ_words + country_words + stop_words


class StemTokenizer(object):
    def __init__(self):
        self.stemmer = SnowballStemmer("english", ignore_stopwords=False)

    def __call__(self, doc):
        return [t for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t) > 1]


