#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 11:34:44 2017

@author: florianmante
"""

#clustering for excel file

import pandas
import numpy as np

from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
#from sklearn import metrics

data = pandas.read_excel("Macroeconomic data/Macroeconomic-data.xls",skiprows=1)

data1 = data.drop(['Unnamed: 0', 'Poverty gap at national poverty lines (%)', 'Poverty gap at $1.90 a day (2011 PPP) (%)'], axis=1)

data2 = data1.dropna(axis=0)
data3 = data2[data2["GINI index (World Bank estimate)"] != "?"]
data4 = data3[data3["GINI index (World Bank estimate)"] != ".."]


reduced_data = np.asarray(data4[data4.columns[1:4]].values, dtype=np.float64)
reduced_data = normalize(reduced_data, axis = 0)
#reduced_data[:,0] = normalize(reduced_data[:,0])
#reduced_data[:,1] = normalize(reduced_data[:,1])
#reduced_data = PCA(n_components=2).fit_transform(reduced_data0)

#%%
#kmeans
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print(__doc__)

kmeans = KMeans(init='k-means++', n_clusters=3, n_init=10)
kmeans.fit(reduced_data)

#predict makes it possible to label the data through the cluster
predict_label = kmeans.predict(reduced_data)

#Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min()-0.1, reduced_data[:, 0].max()+0.1
y_min, y_max = reduced_data[:, 1].min()-0.1, reduced_data[:, 1].max()+0.1
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
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()

#%%
#knearest neighbor

print(__doc__)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors

n_neighbors = 5

# import some data to play with

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

# we create an instance of Neighbours Classifier and fit the data.
#clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
clf = neighbors.NearestNeighbors(n_neighbors, algorithm='auto')
nbrs = clf.fit(reduced_data)
distances, indices = nbrs.kneighbors(reduced_data)
distances
indices

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
#x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
#y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
#xx, yy = np.meshgrid(np.arange(x_min, x_max, 5),
#                     np.arange(y_min, y_max, 1))
##Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#
## Put the result into a color plot
##Z = Z.reshape(xx.shape)
#plt.figure()
##plt.pcolormesh(xx, yy, cmap=cmap_light)
#
## Plot also the training points
#plt.scatter(reduced_data[:, 0], reduced_data[:, 1], cmap=cmap_light)
#plt.xlim(xx.min(), xx.max())
#plt.ylim(yy.min(), yy.max())
#plt.title("3-Class classification (k = %i)"
#          % (n_neighbors))
#
#plt.show()
