"""
===========================================================
compute topics
display topics
===========================================================

important: the dtm matrix
            which is the matrix (num_text, num_feature)
            of large dimensions (390, 13000)
        factorizes this matrix
            LDA method: a probabilistic model capable of expressing 
                        uncertainty about the placement of topics across 
                        texts and the assignment of words to topics
            NMF method: a deterministic algorithm which arrives at a 
                        single representation of the corpus
            both represent "latent topics"

=========== ========================================================

parameters: vectorize method
                TfidfVectorizer prefered
            factorizing
                NMF: non-negative matrix factorization (prefered)
                LDA: latent Dirichlet allocation
            distance between a selected corpus of text
            
            clustering
            
            plot
                        
=========== ========================================================
output: compute topics
        display topics
        display which topics dominates each text of the chosen corpus
=========== ========================================================
"""

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
    def __init__(self, params):
        """
        :param params: dict which contains list of parameters for TopicModelling methods

        Attributes
        ----------
        fileList : list of size m all files (containing reports) that will be open by CountVectorizer
        countries : list of size m country names corresponding to reports in fileList
        vectorizer : instance of class computing document-term matrix from texts
        dtm : m*n array with n size of vocabulary ; document-term matrix :
        dtm[m][n] = frequency of word vocab[n] in fileList[m]
        vocab : list of size n matching index of column with certain word. For instance, vocab[150] = 'growth'
        factorizer : instance of class computing document-topic matrix for document-term matrix
        doctopic : m*d array with d chosen number of topics ; document-topic matrix
        dist : m*m array containing distance between texts
        cluster : instance of class computing clusters between texts
        ----------

        """

        self.params = params
        self.fileList = None
        self.countries = None
        self.vectorizer = None
        self.dtm = None
        self.vocab = None
        self.factorizer = None
        self.doctopic = None
        self.dist = None
        self.cluster = None

    def vectorize(self, technique, fileList, countries):
        """
        Computes the document-term matrix, the vocabulary

        :param technique : {'count_vectorizer','tf-idf'} (default='count_vectorizer')
             Specifies the technique to compute document-term matrix
        :param fileList: value of self.fileList
        :param countries: value of self.countries

        """
        self.fileList = fileList
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
        Computes the document-topic matrix

        :param technique : {'NMF','LDA'} (default='cosine')
             Specifies the technique to compute document-topic matrix
        :param print_topic : if True, print main topic per text and main words in topic
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
        Computes m*m array containing distance between texts
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

    def plot(self, dims=2):
        """
        Plot 2d or 3d representation of data using MDS (or t-SNE?) algorithm
        Parameters
        ----------
        dims : int, {2,3} (default=2)
             Specifies the distance to compute distance matrix

        """
        mds = MDS(n_components=dims, dissimilarity="precomputed", random_state=1)
        pos = mds.fit_transform(self.dist)
        xs, ys = pos[:, 0], pos[:, 1]

        # Ajouter les noms des fichiers : names n'est pas défini. Version 1) voir si ça marche comme ça
        if dims == 2:
            for x, y, name in zip(xs, ys, self.countries):
                plt.scatter(x, y, c=50)
                plt.text(x,y,name)
        elif dims == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])
        else:
            raise ValueError("dims must be 2 or 3")

        plt.show()

