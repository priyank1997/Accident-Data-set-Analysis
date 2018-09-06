# -*- coding: utf-8 -*-
import os
import pandas as pd
import glob
import csv
import numpy as np
import datetime


out=open("combined.csv","rb")
data=csv.reader(out)
i=0
new_data=[[row[4],row[5],row[6],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]] for row in data]
out.close()


out=open("combined.csv","wb")
op=csv.writer(out)
for row in new_data:
    if i>1:
        if row[0]>'2':
            row[0]=3

        d=row[1].split("-")
        if(d[1]=='Jan' or d[1]=='Feb' or d[1]=='Dec'):
            row[1]='WNT'
        elif(d[1]=='May' or d[1]=='Mar' or d[1]=='Apr'):
            row[1]='SPR'
        elif(d[1]=='Jun' or d[1]=='Jul' or d[1]=='Aug'):
            row[1]='SMR'
        else:
            row[1]='FALL'


        row[2]=(int)(row[2])
        if row[2]<=400:
            row[2]='T1'
        elif row[2]<=800 and row[2]>400:
            row[2]='T2'
        elif row[2]>800 and row[2]<=1200:
            row[2]='T3'
        elif row[2]<=1600 and row[2]>1200:
            row[2]='T4'
        elif row[2]<=2000 and row[2]>1600:
            row[2]='T5'
        elif row[2]>2000 and row[2]<=2400:
            row[2]='T6'




        if row[3]=='Dry':
            row[3]='DRY'
        elif row[3]=='Frost / Ice':
            row[3]='ICE'
        elif row[3]=='Snow':
            row[3]='SNOW'
        elif row[3]=='Wet / Damp':
            row[3]='WET'
        else:
            row[3]='FLD'


        if row[4]=='Daylight: no street lighting' or row[4]=='Daylight: street lights present':
            row[4]='DLT'
        elif row[4]=='Darkness: street lights present and lit':
            row[4]='RLT'
        elif row[4]=='Darkness: no street lighting' :
            row[4]='NLT'
        else:
            row[4]='DUS'
        
        
        if row[5]=='Fine without high winds':
            row[5]='FINE'
        elif row[5]=='Fine with high winds':
            row[5]='WIND'
        elif row[5]=='Raining without high winds' or row[5]=='Raining with high winds':
            row[5]='RAIN'
        elif row[5]=='Snowing without high winds' or row[5]=='Snowing with high winds':
            row[5]='SNOW'
        elif row[5]=='Unknown' or row[5]=='Other':
            row[5]='OTH '
        else:
            row[5]='FOG '

        if row[6]=='Driver':
            row[6]='DRIVER'
        elif row[6]=='Passenger':
            row[6]='PASSENGER'
        else:
            row[6]='PEDESTRAIN'

        
        if row[8]=='Male':
            row[8]='M'
        else:
            row[8]='F'


        
        if row[9]<='20':
            row[9]='CHD'
        elif row[9]<='30' and row[9]>'20':
            row[9]='YNU'
        elif row[9]>'30' and row[9]<='60':
            row[9]='ADL'
        elif row[9]>'60':
            row[9]='SNR'

        if row[10]=='Motorcycle - Unknown CC' or row[10]=='Pedal cycle' or row[10]=='M/cycle 50cc and under' or row[10]=='Motorcycle over 50cc and up to 125cc' or row[10]=='Motorcycle over 500cc' or row[10]=='Motorcycle over 125cc and up to 500cc':
            row[10]='TWH'
        elif row[10]=='Taxi/Private hire car' or row[10]=='Car' :
            row[10]='CAR'
        elif row[10]=='Minibus (8 – 16 passenger seats)' or row[10]=='Bus or coach (17 or more passenger seats)':
            row[10]='BUS'
        elif row[10]=='Ridden horse':
            row[10]='ANI'
        elif row[10]=='Agricultural vehicle (includes diggers etc.)' or row[10]=='Goods vehicle over 3.5 tonnes and under 7.5 tonnes mgw' or row[10]=='Goods vehicle 3.5 tonnes mgw and under':
            row[10]='TRC'
        elif row[10]=='Goods vehicle 7.5 tonnes mgw and over':
            row[10]='TOW'
        else:
            row[10]='OTH'
    if i>0:    
        op.writerow(row)
    i=i+1
out.close


out=open("original_combined.csv","rb")
data=csv.reader(out)
i=0
ndata=[[row[4],row[5],row[6],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]] for row in data]
out.close()


out=open("original_combined.csv","wb")
op=csv.writer(out)
for row in ndata:
    if i>1:
        d=row[1].split("-")
        row[1]=d[1]

        row[2]=(int)(row[2])
        row[2]=row[2]/100

    if i>0:    
        op.writerow(row)
    i=i+1
out.close