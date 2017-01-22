import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.manifold import MDS
from sklearn.decomposition import NMF, LatentDirichletAllocation
from preprocessing.load_files import names, fileList


year = str(2013)
X = fileList[year]
names_year = names[year]


# To remove
n_samples = 2000
n_features = 1000
n_topics = 20

class TopicModelling():
    # TODO : update documentation
    """
    Attributes
    ----------
    dtm : TODO

    dist : array, shape = [n,n]
        dist[i][j] = distance between text_i and text_j

    vocab : list, len = p
            Associates the index of each word in the document-term matrix to the word itself
            For instance, if self.dtm[:,1] corresponds to the frequency of the word "banana" in several texts,
            then vocab[1] = "banana"
    """
    def __init__(self,params = None):
        # TODO : how does SKLearn manage this?
        self.params = params

    def vectorize(self, fileList, technique='count_vectorizer'):
        """
        Parameters
        ----------
        raw_documents : iterable, len = n
              an iterable with n file names which yields str
        technique : {'count_vectorizer','tf-idf'} (default='count_vectorizer')
             Specifies the technique to compute document-term matrix

        Returns

        """
        # TODO : check if you must stock transformers
        if technique == 'count_vectorizer':
            vectorizer = CountVectorizer(input='filename', stop_words='english', max_features=500)
        elif technique == 'tf_idf':
            vectorizer = TfidfVectorizer(input='filename', stop_words='english', max_features=500)
        else:
            raise ValueError("technique must belong to {'count_vectorizer','tf-idf'} ")
        # Document-term matrix
        self.dtm = vectorizer.fit_transform(fileList).toarray()
        self.vocab = np.array(vectorizer.get_feature_names())

    def factor(self, technique='NMF'):
        """
        Parameters
        ----------
        technique : {'NMF','LDA'} (default='cosine')
             Specifies the technique to compute document-topic matrix
        """
        if technique == 'NMF':
            # TODO : check if you must stock transformers
           self.doctopic = NMF(n_components=n_topics,
                               random_state=1,
                               alpha=.1,
                               l1_ratio=.5).fit_transform(self.dtm)
        elif technique == 'LDA':
            self.doctopic = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                                      learning_method='online',
                                                      learning_offset=50.,
                                                      random_state=0).fit_transform(self.dtm)
        else:
            raise ValueError("model must belong to {'LDA','NMF'}")

    def distance(self, distance='cosine'):
        """
        Parameters
        ----------
        distance : {'l2','cosine'} (default='cosine')
             Specifies the distance to compute distance matrix
        """
        if distance == 'cosine':
            self.dist = cosine_distances(self.doctopic)
        elif distance == 'l2':
            self.dist = euclidean_distances(self.doctopic)
        else:
            raise ValueError("technique must belong to {'l2','cosine'} ")

    def cluster(self, technique):
        """
        Parameters
        ----------
        technique : {'K-means','Ward'} (default='count_vectorizer')
             Specifies
        """
        # TODO: Complete documentation, complete method
        pass

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
            for x, y, name in zip(xs, ys, names_year):
                plt.scatter(x, y, c=50)
                plt.text(x,y,name)
        elif dims == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
        else:
            raise ValueError("dims must be 2 or 3")

        plt.show()

    def run(self):
        """
        Throws all methods at once

        :return: self
        """
        # TODO : complete documentation, complete method, find better names
        vocab = self.vectorize(X)
        self.factor('NMF')
        self.distance()
        self.plot(2)


params = {
    'vectorize':
        {'technique': 'count_vectorizer',
         'params':
             {


             }

        }

}

tm = TopicModelling()
tm.vectorize(X)


""" TO DO :
- commentaires
- test pour vérifier qu'on a lancé les méthodes une à une
- ajouter noms sur le graphe
- clustering
"""