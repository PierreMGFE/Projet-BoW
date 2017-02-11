#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:10:15 2017

@author: florianmante
"""

import pandas
import numpy as np

def create_data(data1 ="NY.GNP.PCAP.CD", data2 = "NY.GDP.PCAP.KD.ZG", year="2015"):
    #read excel file
    econ_data = pandas.read_excel("Macroeconomic data/Data_Extract_From_World_Development_Indicators (1).xlsx")
    
    #select GNI per capita and not missing data
    econ_data_GNIpc  = econ_data[(econ_data["Series Code"] == data1) & (econ_data[year+" [YR"+year+"]"]!="..")]
    
    #reduce the size with 3 columns
    econ_data_GNIpc_yr = econ_data_GNIpc.loc[:,["Country Name", "Country Code", year+" [YR"+year+"]"]]
    #change the name of columns 2015 to GNI per capita 2015 so as to merge later
    econ_data_GNIpc_yr.rename(columns= {year+" [YR"+year+"]": "GNI per capita "+year}, inplace=True)
    
    #select GDP per capita growth and not missing data
    econ_data_GDPpcGrowth = econ_data[(econ_data["Series Code"] == data2) & (econ_data[year+" [YR"+year+"]"]!="..")]
    econ_data_GDPpcGrowth_yr = econ_data_GDPpcGrowth.loc[:,["Country Name", "Country Code", year+" [YR"+year+"]"]]
    #change the name of columns 2015 to GDP per capita growth 2015 so as to merge later
    econ_data_GDPpcGrowth_yr.rename(columns= {year+" [YR"+year+"]": "GDP per capita growth "+year}, inplace=True)
    
    #merge with country name as key (make sure GNI and GDP correspond to the same country each time)
    econ_data2 = pandas.merge(econ_data_GNIpc_yr, econ_data_GDPpcGrowth_yr, on="Country Name")
    
    #extract GNI per capita and GDP per capita growth as float
    econ_data3 = np.asarray(econ_data2[econ_data2.columns[[2,4]]].values, dtype=np.float64)
    #extract the names of the country corresponding one-to-one to the precedeing array so as to label in a plot
    country_label = np.asarray(econ_data2[econ_data2.columns[0]].values, dtype=str)  
    return econ_data3, country_label

##read excel file
#econ_data = pandas.read_excel("Macroeconomic data/Data_Extract_From_World_Development_Indicators (1).xlsx")
#
##select GNI per capita and not missing data
#econ_data_GNIpc  = econ_data[(econ_data["Series Code"] == "NY.GNP.PCAP.CD") & (econ_data["2015 [YR2015]"]!="..")]
#
##reduce the size with 3 columns
#econ_data_GNIpc_2015 = econ_data_GNIpc.loc[:,["Country Name", "Country Code", "2015 [YR2015]"]]
##change the name of columns 2015 to GNI per capita 2015 so as to merge later
#econ_data_GNIpc_2015.rename(columns= {'2015 [YR2015]': 'GNI per capita 2015'}, inplace=True)
#
##select GDP per capita growth and not missing data
#econ_data_GDPpcGrowth = econ_data[(econ_data["Series Code"] == "NY.GDP.PCAP.KD.ZG") & (econ_data["2015 [YR2015]"]!="..")]
#econ_data_GDPpcGrowth_2015 = econ_data_GDPpcGrowth.loc[:,["Country Name", "Country Code", "2015 [YR2015]"]]
##change the name of columns 2015 to GDP per capita growth 2015 so as to merge later
#econ_data_GDPpcGrowth_2015.rename(columns= {'2015 [YR2015]': 'GDP per capita growth 2015'}, inplace=True)
#
##merge with country name as key (make sure GNI and GDP correspond to the same country each time)
#econ_data2 = pandas.merge(econ_data_GNIpc_2015, econ_data_GDPpcGrowth_2015, on="Country Name")
#
##extract GNI per capita and GDP per capita growth as float
#econ_data3 = np.asarray(econ_data2[econ_data2.columns[[2,4]]].values, dtype=np.float64)
##extract the names of the country corresponding one-to-one to the precedeing array so as to label in a plot
#country_label = np.asarray(econ_data2[econ_data2.columns[0]].values, dtype=str)

#%%

from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
#from sklearn import metrics

econ_data3, country_label = create_data(year="2010")
reduced_data = normalize(econ_data3, axis=0)

#reduced_data = PCA(n_components=2).fit_transform(reduced_data0)

#%%
#kmeans
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print(__doc__)

kmeans = KMeans(init='k-means++', n_clusters=7, n_init=10)
kmeans.fit(reduced_data)

predict_label = kmeans.predict(reduced_data)

#Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 0.1, reduced_data[:, 0].max() + 0.1
y_min, y_max = reduced_data[:, 1].min() - 0.1, reduced_data[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
#fig = plt.figure(1)
fig = plt.Figure(figsize=(10,10),dpi=50)
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
for country in country_label:
    #xpos, ypos = np.random.uniform(-50,50), np.random.uniform(-50,50)
    plt.annotate(country, xy=(reduced_data[i,0], reduced_data[i,1]), xycoords='data', xytext=(+1, +3), textcoords='offset points', fontsize=5,)
    i = i+1

plt.title('K-means clustering\n'
          'normalized (x=GNI per capita, y=GDP per capita growth) \n'
          'for a given year\n'
          'world bank data\n'
          'centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(np.linspace(x_min,x_max,10, endpoint=True))
plt.yticks(np.linspace(y_min,y_max,10, endpoint=True))
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
