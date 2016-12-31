from sklearn.feature_extraction.text import CountVectorizer
from Preprocessing.text_preprocessing import clean_data
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


vectorizer = CountVectorizer()

train_data_features = vectorizer.fit_transform(clean_data)

train_data_features = train_data_features.toarray()

vocab = np.array(vectorizer.get_feature_names())

dist = cosine_distances(train_data_features)

mds = MDS(dissimilarity='precomputed')
pos = mds.fit_transform(train_data_features)

xs, ys = pos[:, 0], pos[:, 1]

plt.scatter(xs, ys)
