#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:37:56 2017

@author: florianmante

===========================================================
transform a  set of PDF files to TXT files
===========================================================

input:  inpath is the path of departure
        from which we look of PDF files
        and transform them to TXT

=========== ========================================================
=========== ========================================================
output: new folder created
        TXT files in the right folder
=========== ========================================================

"""
import os
import re
from settings import ROOT_DIR
import Convert_PDF.filepaths as fpath


def pdf2txt():
    inpath = ROOT_DIR+"/data_files/pdf_data/CAS_CPS_SCD"
    fp = fpath.filepaths(inpath)
    
    for files, path in fp:
        if files.find('.pdf') != -1:
            new_path = re.sub('pdf_data/CAS_CPS_SCD', 'text_data/pdfminer_pdf2txt/CAS_CPS_SCD', path)
            new_path = re.sub(files, '', new_path)
            try: 
                os.makedirs(new_path)
            except OSError:
                if not os.path.isdir(new_path):
                    raise
            txt_name = new_path+re.sub('.pdf','.txt',files)
            os.system(("pdf2txt.py -o %s -t text %s") % (txt_name, path))