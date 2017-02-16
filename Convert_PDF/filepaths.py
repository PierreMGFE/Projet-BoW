"""
===========================================================
give the set of (filename, pathname)
===========================================================

input: top_path is the path from which we want to have every subdirectroy

=========== ========================================================
=========== ========================================================
output: (filename, pathname) as a set
=========== ========================================================
"""


import os


def filepaths(top_path):
    for dirpath, subdirs, files in os.walk(top_path):
        for f in files:
            yield f, os.path.join(dirpath, f)
