# -*- coding: utf-8 -*-

import PyPDF2

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    #content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

print(getPDFContent("C:\Users\Pierre\Downloads\livre_malo.pdf"))