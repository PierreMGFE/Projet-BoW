# -*- coding: utf-8 -*-

import PyPDF2

wd = "C:/Users/Pierre/Documents/ENPC/3. 2A/3. S3/2. TDLOG/Projet Bag of Words/"

def getPDFContent(path):
    content = ""
    num_pages = 2
    p = open(path, "rb")
    # Load PDF into pyPDF
    pdf = PyPDF2.PdfFileReader(p)
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    #content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

print(getPDFContent("SCD_Uruguay_2015.pdf"))


#liste = map(str.strip, liste)

#C:\Users\Pierre\Documents\ENPC\3. 2A\3. S3\2. TDLOG\Projet Bag of Words\Données\CAS_CPS\2000
#C:\Users\Pierre\Documents\ENPC\3. 2A\3. S3\2. TDLOG\Projet Bag of Words\Données\SCD\2016\SCD_Uzbekistan_2016.pdf
#pdf.getNumPages()
#CAS_Djibouti_2005.pdf
#SCD_Uzbekistan_2016.pdf