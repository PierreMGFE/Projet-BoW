#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:53:47 2017

@author: florianmante

===========================================================
display a clustering
    on a given corpus of text (one given year usually)
    in 2d or 3d
===========================================================

input:  doctopic
            a matrix (num_text_corpus, num_topics)
            where each case is the coordinate of the text of the corpus
            is the space of num_topics dimensions
        country_names
            identify each text of the corpus with its name

=========== ========================================================
parameters: reducing data
                if from num_topics > 2 to a 2d graph
                using PCA
    
            kmeans
                number of clusters (3 typically)
                
            a given year for a corpus
=========== ========================================================
output: display 2d or 3d cluster
=========== ========================================================
"""
import importlib
import numpy as np
from sklearn.decomposition import PCA
import d_NLP.topic_modelling.topic_modelling as tm
importlib.reload(tm)


doctopic, topic_words = tm.f_doctopic()
country_names = tm.f_country_names()

#%%
#kmeans two dimensions
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print(__doc__)
reduced_data = PCA(n_components=2).fit_transform(doctopic)

kmeans = KMeans(init='k-means++', n_clusters=3, n_init=10)
kmeans.fit(reduced_data)

#Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
#centroids = kmeans.cluster_centers_
#plt.scatter(centroids[:, 0], centroids[:, 1],
#            marker='x', s=169, linewidths=3,
#            color='w', zorder=10)

i=0
for country in country_names:
    xpos, ypos = np.random.uniform(-50,50), np.random.uniform(-50,50)
    plt.annotate(country, xy=(reduced_data[i,0], reduced_data[i,1]), xycoords='data', xytext=(+xpos,+ypos), textcoords='offset points', fontsize=5,arrowprops=dict(arrowstyle="->"))
    i = i+1

plt.title('K-means clustering (PCA-reduced data)\n'
          'axes are topic related\n'
          'for a given year\n'
          'world bank CAS and SCD\n'
          'centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
#%%
#kmeans three dimensions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

print(__doc__)


kmeans = KMeans(init='k-means++', n_clusters=3, n_init=10)
kmeans.fit(doctopic)

#Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

fig = plt.figure()
plt.clf()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=38, azim=104)

plt.cla()
labels = kmeans.labels_

ax.scatter(doctopic[:, 0], doctopic[:, 1], doctopic[:, 2], c=labels.astype(np.float))

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('topic 0')
ax.set_ylabel('topic 1')
ax.set_zlabel('topic 2')

plt.show()