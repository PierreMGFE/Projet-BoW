from nltk.tokenize import wordpunct_tokenize

from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer


class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in wordpunct_tokenize(doc) if t.isalpha()]


class StemTokenizer(object):
    def __init__(self):
        self.stemmer = SnowballStemmer("english", ignore_stopwords=False)

    def __call__(self, doc):
        return [self.stemmer.stem(t) for t in wordpunct_tokenize(doc) if t.isalpha()]