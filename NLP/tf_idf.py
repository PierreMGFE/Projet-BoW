import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances

from Preprocessing.tokenizers import *
from Preprocessing.text_preprocessing import clean_data


class TopicModelling:
    def __init__(self):
        """
        Attributes
        ----------
        """
        pass

    def fit(self, raw_documents, technique='count_vectorizer'):
        """
        Parameters
        ----------
        raw_documents : iterable, len = n
              an iterable with n texts which yields str
        technique : {'count_vectorizer','tf-idf'} (default='count_vectorizer')
             Specifies the kernel type to be used in the algorithm.

        Returns
        -------
        self : TopicModelling
        """
        if technique == 'count_vectorizer':
            self.vectorizer = CountVectorizer(input='content')
        elif technique == 'tf_idf':
            self.vectorizer = TfidfVectorizer(input='content')
        else:
            raise ValueError("technique must belong to {'count_vectorizer','tf-idf'} ")
        self.dtm = self.vectorizer.fit_transform(raw_documents).toarray()

    def distance(self,distance='cosine'):
        """
        Parameters
        ----------
        distance : {'l2','cosine'} (default='cosine')
             Specifies the distance to compute distance matrix

        Returns
        -------
        dist : array, shape = [n,n]
            dist[i][j] = distance between text_i and text_j
        """
        if distance == 'cosine':
            dist = cosine_distances(self.dtm)
        elif distance == 'l2':
            dist = euclidean_distances(self.dtm)
        else:
            raise ValueError("technique must belong to {'l2','cosine'} ")
        return dist

    def vocab(self):
        """
        Returns
        -------
        vocab : A COMPLETER
        """
        vocab = np.array(self.vectorizer.get_feature_names())
        return vocab


# reduce size of dataset, to reduce overhead
clean_data = clean_data[:10]

tm = TopicModelling()
tm.fit(clean_data)
