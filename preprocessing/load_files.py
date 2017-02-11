import os
from settings import ROOT_DIR
from re import findall


def load_files(path):
    """
     Return a dict representing reco result. This is used in admin interface
     :param path: a string which represents path towards directory containing all files
     :return: a dict named data with every report. data[n][c] contains the report regarding country c in year n.
     For instance, data[2014][Bhutan] contains the 2014 report for Myanmar.
     """
    # TODO : change annotations
    data = dict()
    country_words = []
    for dirpath, dirnames, filenames in os.walk(path):
        year = os.path.basename(dirpath)
        if filenames:
            if year not in data:
                data[year] = dict()
            for filename in filenames:
                cut = filename.split('_')
                country = cut[1]
                split = '[a-zA-Z][^A-Z]*'
                country_words += [word.lower() for word in findall(split, country)]
                file_path = os.path.join(dirpath, filename)
                if country not in data[year]:
                    data[year][country] = file_path
    return data, set(country_words)

path = os.path.join(ROOT_DIR, "text_data/pdftotext")
data, country_words = load_files(path)

