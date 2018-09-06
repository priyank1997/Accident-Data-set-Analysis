import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

from itertools import groupby

import os


dat = pd.read_csv("combined.csv",skiprows=[0])

def similarity_score(x,y):
    count = 0
    for i in range(len(x)):
        if x[i]==y[i]:
            count +=1
    return count

def kmodes(data,clusters,iterations):
    index=np.random.permutation(data.index)[:clusters]#randomly selecting index values for initial k modes
    print ("Randomly selected indexs are : " , index)
    modes=[]
    labels=[]
    dis=[]
    J=[]
    d=dict()
#calculating the dissimilarity score between each categorical object from the modes and assigning label to minimum score
    for i in index:
        modes.append(np.array(data.ix[i]))#inital k modes added 
    print("Cluster heads are : " ,modes)
    for i in range(len(data)):
        dis=[]
        for j in range(len(modes)):
            dis.append(similarity_score(np.array(data.ix[i]),modes[j]))
        labels.append(np.argmin(dis))
    #print("Nearest cluster head array for all rows " , labels)
    #print("Size of lables is ", len(labels))
    data['label']=np.array(labels)
    for j in range(iterations):
        labels=[]
        
        for i in np.unique(data['label']):
            d1=(np.array(data.ix[data['label']==i,:]))
            r=[]
            for l in range(11):
                max=-1
                name='null'
                array=d1[:,l]
                for k, g in groupby(sorted(array)):
                    mm=len(list(g))
                    #print(k,mm,max)
                    
                    if(max<mm):
                        max=mm
                        name=k
                    #print(k , " " ,len(list(g))," ",max," ",name)
                r.append(name)
            modes[i]=np.array(r)
            #print(i)
            #print(r)
            
            #modes.append(np.array(r))
        print(modes)
        for i in range(len(data)):
            di=[]
            for j in range(len(modes)):
                di.append(similarity_score(np.array(data.ix[i,:-1]),modes[j]))
            labels.append(np.argmin(di))
        #print(labels)
        data['label']=np.array(labels)         
            #calculating the diss score between each categorical object and updated modes and assigning new label to minimum score
        print("\n") 
        #print[data['label']]  
        #print(modes)
#calculating the cost function of individual cluster
    for i in range(len(modes)):
        dis=[]
        for j in range(len(data.ix[data['label']==i,:-1])):
            dis.append(similarity_score(np.array(data.ix[data['label']==i,:-1].iloc[j]),modes[i]))
        J.append(sum(dis))
    d['modes']=modes
    d['costfunction']=J
    d['totalcost']=sum(J)
    d['data']=data
    return d

dic = kmodes(dat.ix[:,:],10,5)

print(dic)