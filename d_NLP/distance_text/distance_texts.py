#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:51:22 2016

@author: florianmante

===========================================================
display 2d or 3d distance between texts
===========================================================

parameters: distance
                euclidean
                cosine
                other from sklearn.metrics.pairwise
            project data of N dimensions where N is num_features
                into a plane (2d) or the space (3d) with the MDS
                function
            display            

=========== ========================================================
=========== ========================================================
output: a graph of 2d or 3d
=========== ========================================================
"""
import os
import importlib
from settings import ROOT_DIR
import numpy as np  # a conventional alias
import b_Convert_PDF.filepaths as fpath
importlib.reload(fpath)
import c_preprocessing.tokenizer as tk
import c_preprocessing.vectorizr as vzr
importlib.reload(tk)
importlib.reload(vzr)


inpath = ROOT_DIR+"/a_data/text_data/pdfminer_pdf2txt/CAS_CPS_SCD"

#%%
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

dtm, vocab = vzr.matrix_txt_occurence()

def choose_dist(dtm,dist_type = "cosine"):
    #dist type is either "cosine" or "euclidean"
    if dist_type == "cosine":
        dist = 1 - cosine_similarity(dtm)
    elif dist_type == "euclidean":
        dist = euclidean_distances(dtm)
    return dist
    

#%%

import re
import matplotlib.pyplot as plt

from sklearn.manifold import MDS

dist = choose_dist("cosine", dtm)

# convert 'SCD_Argentina_2000.txt' to 'SCD_Argentina_2000'
names = [re.sub('.txt', '', files) for files, path in fpath.filepaths(inpath)]


def compute_pos2d(dist):
    # two components as we're plotting points in a two-dimensional plane
    # "precomputed" because we provide a distance matrix
    # we will also specify `random_state` so the plot is reproducible.
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    
    pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
    xs, ys = pos[:, 0], pos[:, 1]
    return xs, ys
    
def display_distance_txt2d(dist, names, year):
    #year must be a string "2016" for example
    xs, ys = compute_pos2d(dist)
    for x, y, name in zip(xs, ys, names):
        if year in name:
            color = 'orange' if year in name else 'skyblue'
            plt.scatter(x, y, c=color)
            plt.text(x, y, name)
     
    plt.show()

#%%
import re
from mpl_toolkits.mplot3d import Axes3D

dist = choose_dist("cosine", dtm)
names = [re.sub('.txt', '', files) for files, path in fpath.filepaths(inpath)]

# après Jeremy M. Stober, Tim Vieira
# https://github.com/timvieira/viz/blob/master/mds.py
def compute_pos3d(dist):
    mds = MDS(n_components=3, dissimilarity="precomputed", random_state=1)

    pos = mds.fit_transform(dist)
    return pos
    

def display_distance_txt3d(dist, names, year):
    fig = plt.figure()
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=38, azim=104)
    plt.cla()
    #ax = fig.add_subplot(111, projection='3d')
    pos = compute_pos3d(dist)
    #ax.scatter(pos[:, 0], pos[:, 1], pos[:, 2])

    for x, y, z, s in zip(pos[:, 0], pos[:, 1], pos[:, 2], names):
        if year in s:
            ax.scatter(x,y,z)
            ax.text(x, y, z, s)
    
    plt.show()
