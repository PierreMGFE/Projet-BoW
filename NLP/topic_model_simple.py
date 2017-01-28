import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.manifold import MDS, TSNE
from preprocessing.load_files import fileList,names
from sklearn.decomposition import NMF,LatentDirichletAllocation
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans


year = str(2013)

X = fileList[year]
names_year = names[year]
# t'as changé 2013 en '2013'


pipe = Pipeline([('vectorize', CountVectorizer(input='filename', stop_words='english', max_features=200)),
                 ('topic', NMF(n_components=15)),
                 ('clustering', KMeans())])

data = pipe.fit_transform(X)
