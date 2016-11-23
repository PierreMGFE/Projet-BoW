# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:51:40 2016

@author: florianmante
"""

from PyPDF2 import PdfFileWriter, PdfFileReader 
infile = PdfFileReader(open('projet-BoW-MANTEcopie.pdf', 'rb'))

for i in xrange(infile.getNumPages()):
    p = infile.getPage(i)
    outfile = PdfFileWriter()
    outfile.addPage(p)
    with open('page-%02d.pdf' % i, 'wb') as f:
        outfile.write(f)