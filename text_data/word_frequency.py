#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:51:46 2016

@author: florianmante
"""

#deux moyens de transformer un fichier texte en liste de string
#on utilise le premier moyen
import numpy as np
import nltk

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Il faut retirer les stopwords avant de stemmer

stemmer = SnowballStemmer("english", ignore_stopwords=True)
lemmatizer = WordNetLemmatizer()

#source = ["having", "have", "needs", "need", "inflation", "inflate", "developments", "developing", "aggregation",
#          "aggregated", "population", "poverty", "poor", "poorer", "men", "man", "gases", "gas", "sues", "utilized",
#          "damaged"]
#
#stems1 = [stemmer.stem(word) for word in source]
#stems2 = [lemmatizer.lemmatize(word) for word in source]
#stems3 = [stemmer.stem(word) for word in stems2]
#
#print(stems1)
#print(stems2)
#print(stems3)

def list_file(name_file):
    with open(name_file, "r") as file:
        list_words = file.read().split()
    return list_words
    
#def list_file2(name_file):
#    list_words = np.loadtxt(name_file)
#    return list_words

#pour les fichiers traduit avec procédure: PDFMINER/PDF2TXT
    
#lw_1 = list_file("data/texte_source/pdfminer_pdf2txt/SCD_Myanmar_2014")
#
#mot_avec_tiret = []
#
#for item in lw_1:
#    if "-" in item:
#        mot_avec_tiret.append(item)
#        mot_avec_tiret.append(lw_1[lw_1.index(item)+1])
#        
#mot_sans_tiret = []
#
#for item in mot_avec_tiret:
#    if "-" in item:
#        index_loc = mot_avec_tiret.index(item)
#        item.remove("-")
#        item = item + mot_avec_tiret[index_loc+1]
        
#pour les fichiers traduits avec la procédure PDFTOTEXT

lw_2 = list_file("data/texte_source/pdftotext/SCD/2016/SCD_Afghanistan_2016.pdf.txt")
#lw_2 = list_file("data/texte_source/pdftotext/SCD/2016/SCD_Pacific_2016.pdf.txt")
#lw_2 = list_file("data/texte_source/pdftotext/SCD/2016/SCD_Brazil_2016.pdf.txt")
#cette variable est une liste de string

nltk_lw_2 = nltk.Text(lw_2)
#cette variable est une variable de nature nltk.text,
#donc utilisable par le package nltk

nltk_lw_2_NotDigit = sorted([item for item in nltk_lw_2 if not item.isdigit()])
nltk_lw_2_AlphaBet = sorted([item for item in nltk_lw_2 if item.isalpha()])
nltk_lw_2_AlphaBet_lower = sorted([item.lower() for item in nltk_lw_2_AlphaBet])
nltk_lw_2_AlphaBet_lower_stemmer = sorted([stemmer.stem(word) for word in nltk_lw_2_AlphaBet_lower])


#definition des stopwords
stop = set(nltk.corpus.stopwords.words('english'))
stop_econ = {'figure','percent','growth','public','also'}
nltk_lw_2_AB_WOstop = sorted([item for item in nltk_lw_2_AlphaBet_lower_stemmer if item not in stop and item not in stop_econ and len(item)>1])

fq_lw_2 = nltk.FreqDist(nltk_lw_2_AB_WOstop)#/len(nltk_lw_2_AB_WOstop)

fq_lw_2.plot(50, cumulative=False)
