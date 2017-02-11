import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.manifold import MDS
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.cluster import KMeans
from preprocessing.load_files import data

import preprocessing.tokenizers as tokens
import importlib

importlib.reload(tokens)

year = '2013'
data_year = data[year]

countries = [country for country in data_year.keys()]
reports = [report for report in data_year.values()]


# To remove
n_topics = 3
most_important = 20
n_features = 200

vectorizer = TfidfVectorizer(input='filename', min_df=0.2, max_df=0.8, max_features=n_features, tokenizer=tokens.StemTokenizer())
dtm = vectorizer.fit_transform(reports).toarray()
vocab = list(np.array(vectorizer.get_feature_names()))



