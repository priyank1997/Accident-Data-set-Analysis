import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

from itertools import groupby

import os

#os.chdir(clusters)

dat = pd.read_csv("combined.csv",skiprows=[0])

for l in range(11):
    array=dat.ix[:,l]
    for k, g in groupby(sorted(array)):
        mm=len(list(g))
        print k," ->  ",mm
    print("\n")