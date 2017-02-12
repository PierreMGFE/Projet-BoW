import numpy as np
import preprocessing.load_files as prediction_NLP
from preprocessing.tokenizers import LemmaTokenizer, StemTokenizer
from NLP.topic_model import TopicModelling

import NLP.cluster_GNP_GDP as economic_expost
import sklearn.cluster as clustering

from NLP.display_clustering import display

from argsort_2 import argsort
from sklearn.metrics import adjusted_rand_score



# Import file paths of all reports
year = '2014'
data_year = prediction_NLP.data[year]


wb_reports_paths = [report for report in data_year.values()]
# Names of all countries who had a report written about them
country_names_1 = [country for country in data_year.keys()]

sorting_1, country_names_1 = argsort(country_names_1)
wb_reports_paths = list(np.array(wb_reports_paths)[sorting_1])


# Different parameters for Vectorizer / Factorization
techniques = {'Vectorize' : 'count_vectorizer', 'Factor': 'NMF'}

params = {'Vectorizer':
            {'input': 'filename',
             'max_features': 50,
             'tokenizer': LemmaTokenizer(),
             'max_df': 0.4,
             'min_df': 0.2
            },
          'NMF':
            {'n_components': 3
            },
          'LDA':
          {'n_topics': 3
          },
          'k-Means':
          {'init': 'k-means++',
           'n_clusters': 3,
           'n_init': 10
          },
          'display':
          {
            'most_important' : 20
          }
         }

tm = TopicModelling(params, wb_reports_paths, country_names_1)
tm.vectorize(technique=techniques['Vectorize'])
tm.factor(technique=techniques['Factor'])
tm.clustering()
X_1 = tm.doctopic
cluster_1 = tm.cluster
country_labels_1 = cluster_1.labels_

X_2, country_names_2 = economic_expost.create_data(year)


cluster_2 = clustering.KMeans(**params['k-Means'])
cluster_2.fit(X_2)
country_labels_2 = cluster_2.labels_

sorting_2, country_names_2 = argsort(country_names_2)
country_labels_2 = country_labels_2[sorting_2]
X_2 = X_2[sorting_2]

#print(country_names_1)
#print(country_names_2)

print(adjusted_rand_score(country_labels_1, country_labels_2))

#display(cluster_1, X_1, country_names_1)
    # TODO : add stop
#display(cluster_2, X_2, country_names_2)
