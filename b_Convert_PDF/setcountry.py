#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:36:16 2017

@author: florianmante

===========================================================
Give the set of countries from the names of the PDF files
===========================================================

input:  set of path where PDF files are located


=========== ========================================================
=========== ========================================================
output: a set of country_words
        two same countries appear once only

=========== ========================================================


"""
from settings import ROOT_DIR
import b_Convert_PDF.filepaths as fpath

def set_country():
    inpath = ROOT_DIR+"/a_data/pdf_data/CAS_CPS_SCD"
    
    fp = fpath.filepaths(inpath)
    
    country_words = set()
    
    for files, path in fp:
        if files.find('.pdf') != -1:
            new_files = files[:files.rfind('.pdf')]
            f_str = new_files.split('_')
            ctry_yr = f_str[1]+"_"+f_str[2]
            country_words.add(f_str[1].lower())
            #print(ctry_yr)
    return country_words