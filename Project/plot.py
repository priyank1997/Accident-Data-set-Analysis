import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt
from pandas import Series,DataFrame

from itertools import groupby

import os


os.chdir("clusters")

dat = pd.read_csv("cluster0.csv",skiprows=[0,1])

for l in range(11):
    x=[]
    y=[]
    array=dat.ix[:,l]
    for k, g in groupby(sorted(array)):
        mm=len(list(g))
        x.append(k)
        y.append(mm)
    plt.plot(x, y)
    plt.show()
    print("\n")