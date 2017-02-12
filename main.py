import importlib
import NLP.cluster_GNP_GDP as cluster_1
import NLP.topic_model as cluster_2
from preprocessing.tokenizers import LemmaTokenizer,StemTokenizer

importlib.reload(lf)

year = '2008'
data_year = lf.data[year]

countries = [country for country in data_year.keys()]
reports = [report for report in data_year.values()]

# To remove
n_features = 100
n_topics = 2
most_important = 20

df_max = 0.8
df_min = 0.2

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

tm = cluster_2.TopicModelling(params)
tm.vectorize(reports, technique='count_vectorizer')
tm.factor()
labels = tm.clustering()

if __name__ == '__main__ ':
    displa
