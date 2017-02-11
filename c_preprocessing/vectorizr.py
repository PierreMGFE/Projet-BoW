#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:19:05 2017

@author: florianmante

===========================================================
vectorizes text: tranfrom a TXT file into a vector of features (words)

===========================================================

parameters: vectorizer (Tfidf, Count, Hashing)
            tokenizer
                create the one of your choice in tokenizr.py
                and call it in the function vectorizer()
            stopwords (optional since already stopped in tokenizer)
            minimal frequency
                1%
                or 12 times appeareance
=========== ========================================================
=========== ========================================================
output: give 2 objects
        dtm is a matrix of (num_text, num_feature)
            where a feature is a word in one of the texts
        vocab is the set of features through all the texts
=========== ========================================================
"""
import importlib
from settings import ROOT_DIR
import b_Convert_PDF.filepaths as fpath
importlib.reload(fpath)
import c_preprocessing.tokenizer as tk
importlib.reload(tk)
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def f_filenames(l_years=list(str(year) for year in range(2000,2017))):
    #l_years must be a list of years ["2000", "2001", ...]

    inpath = ROOT_DIR+"/a_data/text_data/pdfminer_pdf2txt/CAS_CPS_SCD"
    
    fp = fpath.filepaths(inpath)
    
    filenames = []
    
    for files, path in fp:
        if path.find('.txt')!=-1:
            for year in l_years:
                if path.find(year)!=-1:
                    filenames.append(path)
    return filenames

def matrix_txt_occurence(vectorizr = "TfidfVectorizer", l_years=list(str(year) for year in range(2000,2017)), tokenizr='First'):
    #l_years must be a list of years ["2000", "2001", ...]

    filenames = f_filenames(l_years)
            
    if vectorizr == "TfidfVectorizer":
        vectorizer = TfidfVectorizer(input='filename',stop_words='english',min_df = 0.2, max_df=0.8,tokenizer = tk.StemTokenizer())        
        #vectorizer = TfidfVectorizer(input='filename',stop_words='english',min_df = 0.2, max_df=0.8,tokenizer = tk.FirstTokenizer())
    elif vectorizr == "CountVecotirzer":
        vectorizer = CountVectorizer(input='filename', stop_words='english', min_df = 0.2, max_df=0.8, tokenizer = tk.FirstTokenizer())
    dtm = vectorizer.fit_transform(filenames)  # a sparse matrix
    vocab = vectorizer.get_feature_names()  # a list
    dtm = dtm.toarray()  # convert to a regular array
    vocab = np.array(vocab)
    return dtm, vocab