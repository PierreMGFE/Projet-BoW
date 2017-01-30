#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 23:49:24 2016

@author: florianmante
"""

import re
import os, errno

## A function to get all of the filepaths
def filepaths(top_path):
    for dirpath, subdirs, files in os.walk(top_path):
        for f in files:
            yield f, os.path.join(dirpath, f)

#
inpath = "/Users/florianmante/Documents/matieres/ponts/3A/TDLOG/projet/data/texte_source/pdftotext"
outpath = "/Users/florianmante/Documents/matieres/ponts/3A/TDLOG/projet/table_ctry_freq/"

fp = filepaths(inpath)

for files, path in fp:
        if files.find('.txt') != -1:
            new_files = files[:files.rfind('.pdf.txt')]
            f_str = new_files.split('_')
            ctry_yr = f_str[1]+"_"+f_str[2]
            print(ctry_yr)
    

