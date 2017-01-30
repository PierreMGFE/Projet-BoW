import os
from settings import ROOT_DIR


def load_files(path):
    """
     Return a dict representing reco result. This is used in admin interface
     :param path: a string which represents path towards directory containing all files
     :return: a dict named data with every report. data[n][c] contains the report regarding country c in year n.
     For instance, data[2014][Bhutan] contains the 2014 report for Myanmar.
     """
    # TODO : change annotations
    data = dict()
    for dirpath, dirnames, filenames in os.walk(path):
        year = os.path.basename(dirpath)
        if filenames:
            if year not in data:
                data[year] = dict()
            for filename in filenames:
                cut = filename.split('_')
                if len(cut) == 3:
                    country = cut[1]
                elif len(cut) > 3:
                    country = cut[1]+'_'+cut[3][0]
                file_path = os.path.join(dirpath, filename)
                data[year][country] = file_path
    return data

path = os.path.join(ROOT_DIR, "text_data/pdftotext")
data = load_files(path)
