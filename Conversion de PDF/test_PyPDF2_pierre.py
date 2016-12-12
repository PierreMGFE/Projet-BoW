# -*- coding: utf-8 -*-

import PyPDF2
import nltk

# import enchant
# d = enchant.Dict("en_US")

wd = "C:/Users/Pierre/Documents/ENPC/3. 2A/3. S3/2. TDLOG/Projet Bow/"

# Données/CAS_CPS
# Données/SCD

def getPDFContent(path):
    content = ""
    # Load PDF into PyPDF2

    pdf = PyPDF2.PdfFileReader(path)
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    # content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content


# PDF to text
output1 = getPDFContent(wd + "Données/CAS_CPS/2000/CAS_Argentina_2000.pdf")
# Erase all non-alphabetic characters
output2 = ''.join([c for c in output1 if c.isalpha() or c == ' '])
# Split the text into a list of lowercase words
output3 = [w.lower() for w in output2.split()]
# Remove words containing less than 3 letters
output4 = [w for w in output3 if len(w) > 2]
# Remove non-english words
# output_set_reduced = [w for w in output_set if d.check(w)]


print(output4)
