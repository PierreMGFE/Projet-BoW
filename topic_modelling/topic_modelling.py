#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:47:06 2016

@author: florianmante
"""
import os
import numpy as np  # a conventional alias
import sklearn.feature_extraction.text as text
from sklearn import decomposition

#%%
from nltk.tokenize import wordpunct_tokenize
from nltk.stem.snowball import SnowballStemmer

spec_words = [ "pdf", "imagebank", "servlet", "wdscontentserver"]
econ_words = ["sector", "percent", "growth","figure", "country"]
country_words = ["botswana", "lesotho", "sudan", "uganda", "mali", "côte", "ivoire", "chad", "brazil", "serbia", "haiti", "bolivia", "tunisia", "bangladesh", "panama", "colombia", "honduras", "costa", "rica", "sri", "lanka", "lebanon", "mauritius", "egypt", "uruguay", "maldives"]
banned_words = spec_words + econ_words + country_words
class StemTokenizer(object):
 def __init__(self):
     self.stemmer = SnowballStemmer("english", ignore_stopwords=False)
 def __call__(self, doc):
     #return [self.stemmer.stem(t) for t in wordpunct_tokenize(doc) if t.isalpha() and t.lower() not in banned_words and len(t)>1] 
     return [t for t in wordpunct_tokenize(doc) if t.isalpha() and (t.lower() not in banned_words) and len(t)>1] 

#%%


CORPUS_PATH = os.path.join('data/texte_source/pdftotext/SCD', '2015')

filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])
filenames.pop(0)
# files are located in data/texte_source/pdftotext/SCD/2016
len(filenames)

filenames[:5]

#vectorizer = text.CountVectorizer(input='filename', stop_words='english', min_df=0.03, tokenizer = StemTokenizer())
vectorizer = text.TfidfVectorizer(input='filename', min_df=0.03, stop_words='english', tokenizer = StemTokenizer())
dtm = vectorizer.fit_transform(filenames).toarray()

vocab = np.array(vectorizer.get_feature_names())

dtm.shape

len(vocab)

num_topics = 3

num_top_words = 30

clf = decomposition.NMF(n_components=num_topics, random_state=1)
#clf = decomposition.LatentDirichletAllocation(n_topics=num_topics, random_state=1)

# this next step may take some time
doctopic = clf.fit_transform(dtm)
# print words associated with topics
topic_words = []

for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([vocab[i] for i in word_idx])

#To make the analysis and visualization of NMF components similar to that of LDA’s topic proportions, we will scale the document-component matrix such that the component values associated with each document sum to one.
doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)

novel_names = []

for fn in filenames:
    basename = os.path.basename(fn)
    name, ext = os.path.splitext(basename)
    name = name.rstrip('0123456789')
    novel_names.append(name)

# turn this into an array so we can use NumPy functions
novel_names = np.asarray(novel_names)

doctopic_orig = doctopic.copy()

# use method described in preprocessing section
num_groups = len(set(novel_names))

doctopic_grouped = np.zeros((num_groups, num_topics))

for i, name in enumerate(sorted(set(novel_names))):
    doctopic_grouped[i, :] = np.mean(doctopic[novel_names == name, :], axis=0)
 
doctopic = doctopic_grouped

novels = sorted(set(novel_names))

print("Top NMF topics in...")

for i in range(len(doctopic)):
    top_topics = np.argsort(doctopic[i,:])[::-1][0:1]
    top_topics_str = ' '.join(str(t) for t in top_topics)
    print("{}: {}".format(novels[i], top_topics_str))
    
#%%    
# show the top 5 words
for t in range(len(topic_words)):
    print("Topic {}: {}".format(t, ' '.join(topic_words[t][:30])))
    
#austen_indices, cbronte_indices = [], []
#
#for index, fn in enumerate(sorted(set(novel_names))):
#    if "Austen" in fn:
#        austen_indices.append(index)
#    elif "CBronte" in fn:
#        cbronte_indices.append(index)
#
#austen_avg = np.mean(doctopic[austen_indices, :], axis=0)
#
#cbronte_avg = np.mean(doctopic[cbronte_indices, :], axis=0)
#
#keyness = np.abs(austen_avg - cbronte_avg)
#
#ranking = np.argsort(keyness)[::-1]  # from highest to lowest; [::-1] reverses order in Python sequences
#
## distinctive topics:
#ranking[:3]
