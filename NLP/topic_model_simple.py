import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.manifold import MDS, TSNE
from preprocessing.text_preprocessing import clean_data
from sklearn.decomposition import NMF,LatentDirichletAllocation
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans


year = '2013'

list_countries = clean_data[year].keys()
list_reports = clean_data[year].values()



pipe = Pipeline([('vectorize', CountVectorizer(input='content', stop_words='english', max_features=200)),
                 ('topic', NMF(n_components=15))])

data = pipe.fit_transform(list_reports)
