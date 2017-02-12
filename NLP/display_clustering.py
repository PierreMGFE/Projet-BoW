import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils.validation import check_is_fitted
import preprocessing.load_files as lf

import preprocessing.tokenizers as tokens




def display(clustering, X, country_labels, step=.01):
    check_is_fitted(clustering, 'cluster_centers_')

    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

    Z = clustering.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)

    fig = plt.Figure(figsize=(10, 10), dpi=50)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    plt.plot(X[:, 0], X[:, 1], 'k.', markersize=2)

    i = 0
    for country in country_labels:
        plt.annotate(country, xy=(X[i,0], X[i,1]), xycoords='data', xytext=(+1, +3),
                     textcoords='offset points', fontsize=8)
        i += 1

    title = 'Clustering \n normalized (x=gni per capita, y=GDP per capita growth)' \
            ' \n for a given year\n world bank data\n'
    plt.title(title)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(np.linspace(x_min,x_max,10, endpoint=True))
    plt.yticks(np.linspace(y_min,y_max,10, endpoint=True))
    plt.show()
