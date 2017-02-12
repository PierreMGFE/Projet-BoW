import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets


def valid_start_clustering(window):
    valid = False
    error_message_text = ""
    # Check if path is valid
    if os.path.isdir(window.folder_path):
        # Check if format is valid
        if (window.format == "pdf" or window.format == "txt"):
            # Check if there are valid files in directory
            if len([file for file in os.listdir(window.folder_path) if file.endswith("." + window.format)]):
                # Check if parameters are valid
                if window.input_param["Vectorizer"]["min_df"] < window.input_param["Vectorizer"]["max_df"]:
                    valid = True
                else:
                    error_message_text += "Check frequency\n"
            else:
                error_message_text += "No " + window.format + " files in directory\n"
        else:
            error_message_text += "Invalid format\n"
    else:
        error_message_text += "Invalid directory\n"

    return valid, error_message_text


def convert_pdf(window):
    os.chdir(window.folder_path)

    if not os.path.isdir("converted"):
        os.mkdir("converted")

    for file in [file for file in os.listdir() if file.endswith(".pdf")]:
        txt_name = "converted/"
        for i in range(len(file) - 4):
            txt_name += file[i]
        txt_name += ".txt"
        try:
            os.system("pdftotext " + file + " " + txt_name)
        except:
            print("Conversion error")



