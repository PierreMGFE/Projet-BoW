import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import cosine_distances

from preprocessing.text_preprocessing import clean_data

vectorizer = CountVectorizer()

train_data_features = vectorizer.fit_transform(clean_data)

train_data_features = train_data_features.toarray()

vocab = np.array(vectorizer.get_feature_names())

dist = cosine_distances(train_data_features)

mds = MDS(dissimilarity='precomputed')
pos = mds.fit_transform(train_data_features)

xs, ys = pos[:, 0], pos[:, 1]

plt.scatter(xs, ys)
