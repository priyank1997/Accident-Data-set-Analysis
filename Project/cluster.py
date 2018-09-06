import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import os

# -*- coding: utf-8 -*-
import glob
import csv
import datetime

def similarity_score(x,y):
    count = 0
    for i in range(len(x)):
        if x[i]==y[i]:
            count +=1
    return count



dat = pd.read_csv("combined.csv",skiprows=[0])

import numpy as np
from kmodes.kmodes import KModes

# random categorical data

km = KModes(n_clusters=6, init='Huang', n_init=5, verbose=1)

clusters = km.fit_predict(dat)

# Print the cluster centroids
clusters=km.cluster_centroids_
print(clusters)
#print(dat)

os.chdir("clusters")
labels=[]
for i in range(len(dat)):
    #print("row is ",dat.ix[i])
    dis=[]
    for j in range(len(clusters)):
        dis.append(similarity_score(np.array(dat.ix[i]),clusters[j]))
    labels.append(np.argmin(dis))  
dat['label']=np.array(labels)
for i in np.unique(dat['label']):
    d1=(np.array(dat.ix[dat['label']==i,:-1]))
    name=str("cluster"+`i`+".csv")
    print(name)
    out=open(name,"wb")
    op=csv.writer(out)
    for row in d1:
        op.writerow(row)
    out.close



