import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.manifold import MDS
from sklearn.decomposition import NMF,LatentDirichletAllocation


# To remove
n_samples = 2000
n_features = 1000
n_topics = 10

class TopicModelling():
    """
    Attributes
    ----------
    dtm : TODO

    dist : array, shape = [n,n]
        dist[i][j] = distance between text_i and text_j
    """
    def __init__(self):
        pass

    def vectorize(self, raw_documents, technique='count_vectorizer'):
        """
        Parameters
        ----------
        raw_documents : iterable, len = n
              an iterable with n texts which yields str
        technique : {'count_vectorizer','tf-idf'} (default='count_vectorizer')
             Specifies the kernel type to be used in the algorithm.

        Returns
        -------
        vocab : list, len = p
                Associates the index of each word in the document-term matrix to the word itself
                For instance, if self.dtm[:,1] corresponds to the frequency of the word "banana" in several texts,
                then vocab[1] = "banana"
        """
        if technique == 'count_vectorizer':
            vectorizer = CountVectorizer(input='content', analyzer='word')
        elif technique == 'tf_idf':
            vectorizer = TfidfVectorizer(input='content')
        else:
            raise ValueError("technique must belong to {'count_vectorizer','tf-idf'} ")
        # Document-term matrix
        self.dtm = vectorizer.fit_transform(raw_documents).toarray()
        vocab = np.array(vectorizer.get_feature_names())
        return vocab

    def distance(self, distance='cosine'):
        """
        Parameters
        ----------
        distance : {'l2','cosine'} (default='cosine')
             Specifies the distance to compute distance matrix
        """
        if distance == 'cosine':
            self.dist = cosine_distances(self.dtm)
        elif distance == 'l2':
            self.dist = euclidean_distances(self.dtm)
        else:
            raise ValueError("technique must belong to {'l2','cosine'} ")

    def factor(self, model):
        """
        Parameters
        ----------
        model : {'NMF','LDA'} (default='cosine')
             Specifies the distance to compute distance matrix
        """
        if model == 'NMF':
            # essayer plusieurs hyperparamètres
           self.factor = NMF(n_components=n_topics,
                             random_state=1,
                             alpha=.1,
                             l1_ratio=.5).fit(self.dtm)
        elif model == 'LDA':
            self.factor = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                                    learning_method='online',
                                                    learning_offset=50.,
                                                    random_state=0).fit(self.dtm)
        else:
            raise ValueError("model must belong to {'LDA','NMF'}")

    def plot(self, dims=2):
        """
        Parameters
        ----------
        dims : int, {2,3} (default=2)
             Specifies the distance to compute distance matrix

        Plot 2d or 3d representation of data using MDS (or t-SNE?) algorithm
        """
        mds = MDS(n_components=dims, dissimilarity="precomputed", random_state=1)
        pos = mds.fit_transform(self.dist)
        xs, ys = pos[:, 0], pos[:, 1]

        # Ajouter les noms des fichiers : names n'est pas défini. Version 1) voir si ça marche comme ça
        if dims == 2:
            plt.scatter(xs, ys)
        elif dims == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
        else:
            raise ValueError("dims must be 2 or 3")
        plt.show()


# reduce size of dataset, to reduce overhead
clean_data = clean_data[:10]

tm = TopicModelling()
vocab = tm.fit(clean_data)
tm.model('NMF')
tm.distance()
tm.plot(2)

""" TO DO :
- commentaires
- test pour vérifier qu'on a lancé les méthodes une à une
- ajouter noms sur le graphe
- clustering
"""