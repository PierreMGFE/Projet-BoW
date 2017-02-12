import importlib

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.preprocessing import normalize


class TopicModelling():
    # TODO : update documentation
    """
    Attributes
    ----------        print('Top {0} words for each topic'.format(most_important))

    dtm : TODO

    dist : array, shape = [n,n]
        dist[i][j] = distance between text_i and text_j

    vocab : list, len = p
            Associates the index of each word in the document-term matrix to the word itself
            For instance, if self.dtm[:,1] corresponds to the frequency of the word "banana" in several texts,
            then vocab[1] = "banana"
    """
    def __init__(self, params, fileList, countries):
        # TODO : how does SKLearn manage this?
        self.params = params
        self.fileList = fileList
        self.countries = countries

    def vectorize(self, technique):
        """
        Parameters
        ----------
        raw_documents : iterable, len = n
              an iterable with n file names which yields str
        technique : {'count_vectorizer','tf-idf'} (default='count_vectorizer')
             Specifies the technique to compute document-term matrix

        Returns

        """
        # TODO : change year
        if technique == 'CountVectorizer':
            self.vectorizer = CountVectorizer(**self.params['Vectorizer'])
        elif technique == 'TF-IDF':
            self.vectorizer = TfidfVectorizer(**self.params['Vectorizer'])
        else:
            raise ValueError("technique must belong to {'count_vectorizer','tf-idf'} ")
        # Document-term matrix
        self.dtm = self.vectorizer.fit_transform(self.fileList).toarray()
        self.vocab = list(self.vectorizer.get_feature_names())

    def factor(self, technique, print_topic=True):
        """
        Parameters
        ----------
        technique : {'NMF','LDA'} (default='cosine')
             Specifies the technique to compute document-topic matrix
        """
        if technique == 'NMF':
            # TODO : check if you must stock transformers
           self.factorizer = NMF(**self.params['NMF'])
        elif technique == 'LDA':
            self.factorizer = LatentDirichletAllocation(**self.params['LDA'])
        else:
            raise ValueError("model must belong to {'LDA','NMF'}")
        self.doctopic = self.factorizer.fit_transform(self.dtm)
        most_important = self.params['display']['most_important']
        self.doctopic = normalize(self.doctopic,axis=0)
        if print_topic:
            print('Top {0} words for each topic'.format(most_important))
            words_topic = self.factorizer.components_
            # TODO : utile de trier ici ?
            sorted_words = np.argsort(words_topic, 1)
            n = list(self.params[technique].values())[0]
            for i in np.arange(n):
                vocab_topic = [self.vocab[topic_word] for topic_word in sorted_words[i]]
                print('Topic {0}'.format(i))
                print(*vocab_topic[:most_important])
                print('\n')

            major_topics = np.argmax(self.doctopic, 1)
            for i in np.arange(len(self.countries)):
                print('Major topic for {0} : {1}'.format(self.countries[i], major_topics[i]))

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

    def clustering(self):

        self.cluster = KMeans(**self.params['k-Means'])
        self.cluster.fit(self.doctopic)

    def plot(self, countries, dims=2):
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
            for x, y, name in zip(xs, ys, countries):
                plt.scatter(x, y, c=50)
                plt.text(x,y,name)
        elif dims == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
        else:
            raise ValueError("dims must be 2 or 3")

        plt.show()

