# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 20:01:11 2023

@author: Dell
"""

import numpy as np 
import matplotlib as plt
import pandas as pd
import geopandas as gpd

from shapely.geometry import Point, Polygon

def shannon(lc):
    ind=[]
    a=lc['Final']
    
    value=a.value_counts()
    for v in value:
        #print(v)
        pi=v/sum(value)
        
   
        ln_pi=np.log(pi)
    
        mul=-(pi*ln_pi)
        #print('(pi is :%f , log pi is :%f, multiply of pi and log pi is: %f)' %(pi,ln_pi, mul))
        ind.append(mul)
   
    shanon=np.sum(ind)
    #print("the shanon index is:", shanon)
   
    return (shanon)    



lc=gpd.read_file('C:\\Users\\Dell\\Downloads\\germanyhiwi\\germanyhiwi.shp')
points=gpd.read_file("C:\\Users\\Dell\\Downloads\\germanyhiwi\\Germanyplots.shp")
prog_points=points.to_crs(25832)
# ax1 = lc.plot()   # plot the polygon
# lc.plot(ax=ax1, color='red', zorder=15)         # plot red points
# prog_points.plot(ax=ax1, color='yellow', zorder=6)  # plot yellow point

sh=[]

for ind,rows_point in prog_points.iterrows():
 
    plot=[]
    
    for ind,rows_poly in lc.iterrows():
        if rows_point['Plot']==rows_poly['plotID']:
            #print(rows_point['Plot'],rows_poly['plotID'])
            
            plot.append(rows_poly)
            df=gpd.GeoDataFrame(plot)
            df['area percentage']=(df['Area']/df['Area'].sum())*100
        
    
    
    sh.append(shannon(df))
    
    
    
    filename='D:\\work\\hiwi\\germanyhiwi\\final\\Germany\\Excel files\\'+rows_point['Plot']+".xlsx"
    shapefile="D:\\work\\hiwi\\germanyhiwi\\final\\Germany\\Shapefiles\\"+rows_point['Plot']+".shp"   
    df.to_excel(filename) 
    df.to_file(shapefile)   
    
    #print("the shanon index of",rows_point['Plot'], "is:", sh)

shan=pd.DataFrame(sh)
fn="D:\\work\\hiwi\\germanyhiwi\\final\\Germany\\shannon.xlsx"
shan.to_excel(fn)

    

    
 
