import preprocessing.load_files as prediction_NLP
from preprocessing.tokenizers import LemmaTokenizer, StemTokenizer
from NLP.topic_model import TopicModelling

import NLP.cluster_GNP_GDP as economic_expost
import sklearn.cluster as clustering

from NLP.display_clustering import display



# Import file paths of all reports
year = '2008'
data_year = prediction_NLP.data[year]


wb_reports_paths = [report for report in data_year.values()]
# Names of all countries who had a report written about them
country_names_1 = [country for country in data_year.keys()]


# Different parameters for Vectorizer / Factorization
params = {'Vectorizer' :
          {'input' : 'filename',
           'max_features' : 100,
           'tokenizer': LemmaTokenizer(),
           'max_df': 0.8,
           'min_df': 0.2
          },
          'Factorization' :
          {
           'n_topics' : 3
          }
         }

tm = TopicModelling(params)
tm.vectorize(wb_reports_paths, technique='count_vectorizer')
tm.factor()
tm.clustering()
X_1 = tm.doctopic
cluster_1 = tm.cluster
country_labels_1 = cluster_1.labels_

X_2,country_names_2 = economic_expost.create_data('2009')


cluster_2 = clustering.KMeans(init='k-means++', n_clusters=5, n_init=10)
cluster_2.fit(X_2)
country_labels_2 = cluster_2.labels_


if __name__ == '__main__ ':
    display(cluster_1, X_1, country_names_1)
    # TODO : add stop
    display(cluster_2, X_2, country_names_2)