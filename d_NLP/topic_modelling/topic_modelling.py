#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:47:06 2016

@author: florianmante

===========================================================
compute topics
display topics
===========================================================

input:  takes the dtm matrix
            which is the matrix (num_text, num_feature)
            of large dimensions (390, 13000)
        factorizes this matrix
            LDA method: a probabilistic model capable of expressing 
                        uncertainty about the placement of topics across 
                        texts and the assignment of words to topics
            NMF method: a deterministic algorithm which arrives at a 
                        single representation of the corpus
            both represent "latent topics"

=========== ========================================================

parameters: factorizing
                NMF: non-negative matrix factorization (prefered)
                LDA: latent Dirichlet allocation
            vectorizer method
                TfidfVectorizer prefered
            num_topics: 
                number of topics chosen
            num_top_words: 
                number of words defining one topic
            
            l_years
                years of study constituting the corpus
            
=========== ========================================================
output: compute topics
        display topics
        display which topics dominates each text of the chosen corpus
=========== ========================================================
"""
import os
import importlib
import numpy as np  # a conventional alias
from sklearn import decomposition
import c_preprocessing.vectorizr as vzr
importlib.reload(vzr)

#%%

def f_clf(l_years=["2005"], num_topics=3, num_top_words=30, method="NMF", vectorizr="TfidfVectorizer"):
    dtm, vocab = vzr.matrix_txt_occurence("TfidfVectorizer",l_years)

    if method == "NMF":
        clf = decomposition.NMF(n_components=num_topics, random_state=1)
    elif method == "LDA":
        clf = decomposition.LatentDirichletAllocation(n_topics=num_topics, random_state=1)
       
    return clf, dtm, vocab
    
def f_doctopic(l_years=["2005"], num_topics=3, num_top_words=30, method="NMF", vectorizr="TfidfVectorizer"):
    #transform a matrix into groups of main topics
    clf, dtm, vocab = f_clf(l_years, num_topics, num_top_words, method, vectorizr)
    # this next step may take some time
    doctopic = clf.fit_transform(dtm)
    #To make the analysis and visualization of NMF components similar to that of LDA’s topic proportions, we will scale the document-component matrix such that the component values associated with each document sum to one.
    doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)

    topic_words = []

    for topic in clf.components_:
        word_idx = np.argsort(topic)[::-1][0:num_top_words]
        topic_words.append([vocab[i] for i in word_idx])
        
    return doctopic, topic_words
    
#def f_topic_words(l_years=["2005"], num_topics=3, num_top_words=30, method="NMF", vectorizr="TfidfVectorizer"):
## print words associated with topics
#    clf, dtm, vocab = f_clf()
#    topic_words = []
#
#    for topic in clf.components_:
#        word_idx = np.argsort(topic)[::-1][0:num_top_words]
#        topic_words.append([vocab[i] for i in word_idx])
#    return topic_words

def f_country_names(l_years=["2005"]):
    country_names = []
    
    filenames = vzr.f_filenames(l_years)
    
    for file in filenames:
        basename = os.path.basename(file)
        name, ext = os.path.splitext(basename)
        #name = name.rstrip('0123456789')
        country_names.append(name)
    
    # turn this into an array so we can use NumPy functions
    country_names = np.asarray(country_names)
    return country_names
    
def display_topic(num_topics=3, num_top_words=30, method="NMF"):
    doctopic,topic_words = f_doctopic()
    #doctopic_orig = doctopic.copy()

    # use method described in preprocessing section
    country_names = f_country_names()
    num_groups = len(set(country_names))

    doctopic_grouped = np.zeros((num_groups, num_topics))

    for i, name in enumerate(sorted(set(country_names))):
        doctopic_grouped[i, :] = np.mean(doctopic[country_names == name, :], axis=0)
 
    doctopic = doctopic_grouped
    
    countries = sorted(set(country_names))

    print("Top "+method+" topics in...")
    
    for i in range(len(doctopic)):
        top_topics = np.argsort(doctopic[i,:])[::-1][0:1]
        top_topics_str = ' '.join(str(t) for t in top_topics)
        print("{}: {}".format(countries[i], top_topics_str))
           
    #topic_words = f_topic_words()
    # show the top 5 words
    for t in range(len(topic_words)):
        print("Topic {}: {}".format(t, ' '.join(topic_words[t][:num_top_words])))
    
display_topic()
