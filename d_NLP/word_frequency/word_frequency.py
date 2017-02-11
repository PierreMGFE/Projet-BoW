#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:51:46 2016

@author: florianmante

===========================================================
display top words from a given text with a diagram
===========================================================

function:   list_file
                transform the TXT file into a list of words
            transform it into an NLTK readable format
            
            tokenize the txt
            
            display top words

=========== ========================================================
=========== ========================================================
output: display top words for one given text
=========== ========================================================
"""

#deux moyens de transformer un fichier texte en liste de string
#on utilise le premier moyen
#import numpy as np
import importlib
import nltk
import g_User_interaction.choose_cntry_yr as ccy #User_interaction/...
importlib.reload(ccy)

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Il faut retirer les stopwords avant de stemmer

stemmer = SnowballStemmer("english", ignore_stopwords=True)
lemmatizer = WordNetLemmatizer()


def list_file(name_file):
    with open(name_file, "r") as file:
        list_words = file.read().split()
    return list_words
    

#definition des stopwords
stop_english = set(nltk.corpus.stopwords.words('english'))
stop_econ = {'figure','percent','growth','public','also'}


def tokenize_txt(path,nodigit=True,alpha=True,len_min=1,lower=True,stemming=True,stopwords=True):
    list_words = list_file(path)
    nltk_lw = nltk.Text(list_words)
    if nodigit:
        nltk_lw = sorted([item for item in nltk_lw if not item.isdigit()])
    if alpha:
        nltk_lw = sorted([item for item in nltk_lw if item.isalpha()])
    if len_min > 0:
        nltk_lw = sorted([item for item in nltk_lw if len(item)>len_min])
    if lower:
        nltk_lw = sorted([item.lower() for item in nltk_lw])
    if stemming:
        nltk_lw = sorted([stemmer.stem(word) for word in nltk_lw])
    if stopwords:
        nltk_lw = sorted([item for item in nltk_lw if item not in stop_english and item not in stop_econ])
    return nltk_lw
    
def affiche(tokenize_txt, number=50):
    fq_lw = nltk.FreqDist(tokenize_txt)
    fq_lw.plot(number, cumulative = False)
    
 
#%%

country, year = ccy.country_year()
file, path = ccy.give_file_path(country, year)
token_txt = tokenize_txt(path)
affiche(token_txt)
        
        
        
