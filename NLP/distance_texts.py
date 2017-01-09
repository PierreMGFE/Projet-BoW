#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:51:22 2016

@author: florianmante
"""
import numpy as np  # a conventional alias
import files_names as fn
import nltk
from nltk.tokenize import wordpunct_tokenize

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer



inpath = "/Users/florianmante/Documents/matieres/ponts/3A/TDLOG/projet/data/texte_source/pdftotext"


fp = fn.filepaths(inpath)

filenames = []

for files, path in fp:
    if path.find('.pdf.txt')!=-1:
        filenames.append(path)
        
        
    
#%%
#define the tokenizer of your choice

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
#%%
#use the CountVectorizer method
vectorizer = CountVectorizer(input='filename', stop_words='english', min_df = 12, tokenizer = StemTokenizer())

dtm = vectorizer.fit_transform(filenames)  # a sparse matrix

vocab = vectorizer.get_feature_names()  # a list

#%%
#use the tf-idf method

vectorizer = TfidfVectorizer(input='filename', min_df=0.03, stop_words='english',tokenizer = StemTokenizer())

dtm = vectorizer.fit_transform(filenames)

vocab = vectorizer.get_feature_names()  # a list

#%%
# for reference, note the current class of `dtm`
type(dtm)

dtm = dtm.toarray()  # convert to a regular array

vocab = np.array(vocab)

#%%

# the first file, indexed by 0 in Python, is *Emma*
#filenames[0] == 'data/austen-brontë/Austen_Emma.txt'

# use the standard Python list method index(...)
# list(vocab) or vocab.tolist() will take vocab (an array) and return a list
water_idx = list(vocab).index('water')

dtm[0, water_idx]

# using NumPy indexing will be more natural for many
# in R this would be essentially the same, dtm[1, vocab == 'house']
dtm[0, vocab == 'water']

#%%

# "by hand"
n, _ = dtm.shape

dist = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        x, y = dtm[i, :], dtm[j, :]
        dist[i, j] = np.sqrt(np.sum((x - y)**2))


from sklearn.metrics.pairwise import euclidean_distances

dist = euclidean_distances(dtm)

np.round(dist, 1)
#Out[19]: 
#array([[    0. ,  3856.3,  4182.8,  5119.7,  7113.3,  5280.2],
#       [ 3856.3,     0. ,  1922.6,  6313.1,  4126.2,  6381.2],
#       [ 4182.8,  1922.6,     0. ,  6657.4,  4045.3,  6650.3],
#       [ 5119.7,  6313.1,  6657.4,     0. ,  8363.8,  2591.5],
#       [ 7113.3,  4126.2,  4045.3,  8363.8,     0. ,  8484.1],
#       [ 5280.2,  6381.2,  6650.3,  2591.5,  8484.1,     0. ]])

# *Pride and Prejudice* is index 1 and *Jane Eyre* is index 3
#filenames[1] == 'data/austen-brontë/Austen_Pride.txt'
#Out[20]: True

#filenames[3] == 'data/austen-brontë/CBronte_Jane.txt'
#Out[21]: True

# the distance between *Pride and Prejudice* and *Jane Eyre*
dist[1, 3]
#Out[22]: 6313.0833987838305

# which is greater than the distance between *Jane Eyre* and *Villette* (index 5)
dist[1, 3] > dist[3, 5]
#Out[23]: True

#%%

from sklearn.metrics.pairwise import cosine_similarity

dist = 1 - cosine_similarity(dtm)

np.round(dist, 2)
#Out[26]: 
#array([[-0.  ,  0.02,  0.03,  0.05,  0.06,  0.05],
#       [ 0.02,  0.  ,  0.02,  0.05,  0.04,  0.04],
#       [ 0.03,  0.02,  0.  ,  0.06,  0.05,  0.05],
#       [ 0.05,  0.05,  0.06,  0.  ,  0.02,  0.01],
#       [ 0.06,  0.04,  0.05,  0.02, -0.  ,  0.01],
#       [ 0.05,  0.04,  0.05,  0.01,  0.01, -0.  ]])

# the distance between *Pride and Prejudice* (index 1)
# and *Jane Eyre* (index 3) is
dist[1, 3]
#Out[27]: 0.047026234323162663

# which is greater than the distance between *Jane Eyre* and
# *Villette* (index 5)
dist[1, 3] > dist[3, 5]
#Out[28]: True

#%%

import os  # for os.path.basename

import matplotlib.pyplot as plt

from sklearn.manifold import MDS

# two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]

# short versions of filenames:
# convert 'data/austen-brontë/Austen_Emma.txt' to 'Austen_Emma'
names = [os.path.basename(fn).replace('/Users/florianmante/Documents/matieres/ponts/3A/TDLOG/projet/data/texte_source/pdftotext', '') for fn in filenames]

# color-blind-friendly palette
for x, y, name in zip(xs, ys, names):
    if "2016" in name:
        color = 'orange' if "2016" in name else 'skyblue'
        plt.scatter(x, y, c=color)
        plt.text(x, y, name)
 

plt.show()

#%%

# après Jeremy M. Stober, Tim Vieira
# https://github.com/timvieira/viz/blob/master/mds.py
mds = MDS(n_components=3, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
#Out[48]: <mpl_toolkits.mplot3d.art3d.Path3DCollection at 0x2b96c03c1470>

for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
    if "2003" in s:
            ax.text(x, y, z, s)

plt.show()
