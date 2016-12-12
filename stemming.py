#Voir paragraphe "3.6 Normalizing Text", page 107 de NLP with Python


from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

# Il faut retirer les stopwords avant de stemmer

stemmer = SnowballStemmer("english", ignore_stopwords=True)
lemmatizer = WordNetLemmatizer()

source = ["having", "have", "needs", "need", "inflation", "inflate", "developments", "developing", "aggregation",
          "aggregated", "population", "poverty", "poor", "poorer", "men", "man", "gases", "gas", "sues", "utilized",
          "damaged"]

stems1 = [stemmer.stem(word) for word in source]
stems2 = [lemmatizer.lemmatize(word) for word in source]
stems3 = [stemmer.stem(word) for word in stems2]

print(stems1)
print(stems2)
print(stems3)


