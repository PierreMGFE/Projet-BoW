import os,sys,time
pdfs = [file for file in os.listdir() if file.endswith(".pdf")]
if not os.path.isdir("converted"):
    os.mkdir("converted")
for file in pdfs:
    txt_name = "converted/"
    for i in range(len(file)-4):
        txt_name += file[i]
    txt_name += ".txt"
    os.system("pdftotext " + file + " " + txt_name)

