from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import wordpunct_tokenize

from preprocessing.load_files import country_words


# List of banned words that we will remove from reports
stop_words = list(stopwords.words('english'))
spec_words = ["pdf", "imagebank", "servlet", "wdscontentserver", 'aaa', 'access', 'also',
              'achieved', 'ida', 'ifc', 'ii', 'ta', 'wbg', 'us', 'caspr', 'cascr', 'gpoba']
econ_words = ["sector", "percent", "figure", "country", "bank", 'cps', 'development', 'government',
              'management', 'program', 'project', 'public', 'services', 'support']
banned_words = spec_words + econ_words + list(country_words) + stop_words


"""
Differents tokenizers : remove punctuation, lower case, remove words that are banned
or that are too short
"""

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t) > 4]


class StemTokenizer(object):
    def __init__(self):
        self.stemmer = SnowballStemmer("english", ignore_stopwords=False)

    def __call__(self, doc):
        return [t for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t) > 4]


class FirstTokenizer(object):
    def __init__(self):
        self.stemmer = SnowballStemmer("english", ignore_stopwords=False)

    def __call__(self, doc):
        return [t for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t) > 4 ]