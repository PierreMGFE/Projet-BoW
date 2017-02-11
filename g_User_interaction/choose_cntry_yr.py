#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:39:55 2017

@author: florianmante

===========================================================
give (filename, pathname) of a given country for a given year
===========================================================

input:  ask the user a country and a year
        with the correct orthograph
            upper case and so on

=========== ========================================================
ADD ERRORs CHECK and EXCEPTIONS
=========== ========================================================
output: (filename, pathname) for 1 country and 1 year
=========== ========================================================
"""
import importlib
from settings import ROOT_DIR
import b_Convert_PDF.filepaths as fpath
importlib.reload(fpath)

def country_year():       
    country = input("Enter the name of a country: ")
    year = input("Enter a year: ")
    return country, year

def give_file_path(country, year, forma = '.txt'):
    inpath = ROOT_DIR+"/a_data/text_data/pdfminer_pdf2txt/CAS_CPS_SCD"
    fp = fpath.filepaths(inpath)
    for files, path in fp:
        if files.find(country) != -1 and files.find(year) != -1 and files.find(forma) != -1:
            return files, path