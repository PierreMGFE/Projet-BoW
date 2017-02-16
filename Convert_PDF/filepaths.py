import os


def filepaths(top_path):
    for dirpath, subdirs, files in os.walk(top_path):
        for f in files:
            yield f, os.path.join(dirpath, f)
