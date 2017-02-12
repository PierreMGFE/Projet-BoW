import importlib

import matplotlib.pyplot as plt
import numpy as np
from preprocessing.load_files import data
from sklearn.feature_extraction.text import TfidfVectorizer
import preprocessing.tokenizers as tokens
importlib.reload(tokens)

year = '2006'
data_year = data[year]

countries = [country for country in data_year.keys()]
reports = [report for report in data_year.values()]


# To remove
n_topics = 3
most_important = 20
n_features = 50

vectorizer = TfidfVectorizer(input='filename', min_df=0.2, max_df=0.7, max_features=n_features, tokenizer=tokens.StemTokenizer())
dtm = vectorizer.fit_transform(reports).toarray()
vocab = list(np.array(vectorizer.get_feature_names()))


def display_distance_txt3d(dist, names, year):
    fig = plt.figure()
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=38, azim=104)
    plt.cla()
    # ax = fig.add_subplot(111, projection='3d')
    pos = compute_pos3d(dist)
    # ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
    for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
        if year in s:
            ax.scatter(x, y, z)
            ax.text(x, y, z, s)
    plt.show()


def display_distance_txt2d(dist, names, year):

    xs, ys = compute_pos2d(dist)
    for x, y, name in zip(xs, ys, names):
        if year in name:
            color = 'orange' if year in name else 'skyblue'
            plt.scatter(x, y, c=color)
            plt.text(x, y, name)
        plt.show()