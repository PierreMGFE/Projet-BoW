from PyPDF2 import PdfFileWriter, PdfFileReader
infile = PdfFileReader(open('projet-BoW-MANTEcopie.pdf', 'rb'))

for i in range(infile.getNumPages()):
    p = infile.getPage(i)
    outfile = PdfFileWriter()
    outfile.addPage(p)
    with open('page-%02d.pdf' % i, 'wb') as f:
        outfile.write(f)