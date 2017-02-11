#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:15:41 2017

@author: florianmante

===========================================================
class of tokenizing and stemming of our choice
===========================================================

parameters: stemmer from NLTK
                WordNetLemmatizer uses the web a source
                SnowballStemmer is a program
            tokenizing
                keep only words not number
                get rid of the punctuation
                words of length 3 minimal
            stopwords
                country
                too regular and unessential words
                technical words from PDF
=========== ========================================================
=========== ========================================================
output: class callable in vectorizer or anywhere where usefull
=========== ========================================================

"""
import importlib
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import wordpunct_tokenize
import b_Convert_PDF.setcountry as sc
importlib.reload(sc)



spec_words = [ "pdf", "imagebank", "servlet", "wdscontentserver"]
econ_words = ["sector", "percent", "growth","figure", "country"]
country_words = list(sc.set_country())+["sri", "lanka", "côte", "ivoire", "costa", "rica", "bosnia", "herzegovina", "salvador", "oecs", "sao", "tome", "principe", "sierra", "leone", "timor", "leste", "burkina", "faso", "dominican"]
stop_english = list(stopwords.words('english'))
banned_words = spec_words + econ_words + country_words+stop_english


class LemmaTokenizer(object):
 def __init__(self):
     self.wnl = WordNetLemmatizer()
 def __call__(self, doc):
     return [self.wnl.lemmatize(t) for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t)>2]
             

class StemTokenizer(object):
 def __init__(self):
     self.stemmer = SnowballStemmer("english", ignore_stopwords=False)
 def __call__(self, doc):
     return [self.stemmer.stem(t) for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t)>2]
     
     
class FirstTokenizer(object):
 def __init__(self):
     self.stemmer = SnowballStemmer("english", ignore_stopwords=False)
 def __call__(self, doc):
     return [t for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t)>2]