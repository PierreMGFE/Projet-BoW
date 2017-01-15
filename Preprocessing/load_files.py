import os
from settings import ROOT_DIR


def load_file(name_file):
    """
    Return a list of all words in a file
    :param name_file : string -> path towards the file
    :return: list -> contains all words in file
    """
    with open(name_file, "r") as file:
        text = file.read()
    return text


def load_files(path):
    """
     Return a dict representing reco result. This is used in admin interface
     :param path: a string which represents path towards directory containing all files
     :return: a dict named data with every report. data[n][c] contains the report regarding country c in year n.
     For instance, data[2014][Bhutan] contains the 2014 report for Myanmar.
     """
    data = dict()
    for dirpath, dirnames, filenames in os.walk(path):
        year = os.path.basename(dirpath)
        if year not in data and filenames:
            data[year]=dict()
        for filename in filenames:
            try:
                country = filename.split('_')[1]
                text = load_file(os.path.join(dirpath, filename))
                data[year][country] = text
            except UnicodeDecodeError:
                pass
    return data


path = os.path.join(ROOT_DIR, "text_data/pdftotext")
data = load_files(path)
