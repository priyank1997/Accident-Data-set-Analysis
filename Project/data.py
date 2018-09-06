
import os
import pandas as pd
import glob
import csv
import numpy as np
import datetime

print('Hi_start')

os.chdir("dataset")
fileList=glob.glob("*.csv")
dfList = pd.DataFrame([])
i=0
for filename in fileList:
    print(filename)
    if i==0:
        df=pd.read_csv(filename,header=None)
    else:    
        df=pd.read_csv(filename,header=None,skiprows=1)
    dfList=dfList.append(df)
    i=i+1
os.chdir("..")
dfList.to_csv('combined.csv')
dfList.to_csv('original_combined.csv')

