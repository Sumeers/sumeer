#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np 
import matplotlib as plt
import pandas as pd
import geopandas as gpd
get_ipython().run_line_magic('matplotlib', 'inline')
from shapely.geometry import Point, Polygon


# In[3]:


lc=gpd.read_file('C:/Users/Dell/Downloads/Testhiwi/bwkhab.shp')
lc_utm = lc.to_crs({'init': 'epsg:31370'})
lc_utm.plot()


# In[5]:


print(lc.crs)
print("----------")

print(lc_utm.crs)


# In[6]:


point=pd.read_csv('C:/Users/Dell/Downloads/Testhiwi/points.csv')

crs={'init':'epsg:4326'}
geometry=[Point(xy) for xy in zip(point["long"], point["lat"])]
geodata=gpd.GeoDataFrame(point,crs=crs, geometry=geometry)

point_wgs = geodata.to_crs({'init': 'epsg:31370'})
point_wgs.plot()


# In[19]:


buffer=point_wgs.buffer(500)
buffer.plot()


# In[21]:


def join(clipped):
    print("clipping")
    clas=pd.read_csv('C:/Users/Dell/Downloads/Testhiwi/class.csv', encoding = 'latin')
    head1=clipped.join(clas.set_index("Dutch"), on="EENH1")
    head1['eng1']=head1['English description']
    head2=clipped.join(clas.set_index("Dutch"), on="EENH2")
    head2['eng2']=head2['English description']
    head3=clipped.join(clas.set_index("Dutch"), on="EENH3")
    head3['eng3']=head3['English description']
    head4=clipped.join(clas.set_index("Dutch"), on="EENH4")
    head4['eng4']=head4['English description']
    head5=clipped.join(clas.set_index("Dutch"), on="EENH5")
    head5['eng5']=head5['English description']
    head6=clipped.join(clas.set_index("Dutch"), on="EENH6")
    head6['eng6']=head6['English description']
    head7=clipped.join(clas.set_index("Dutch"), on="EENH7")
    head7['eng7']=head7['English description']
    head8=clipped.join(clas.set_index("Dutch"), on="EENH8")
    head8['eng8']=head8['English description']
    head=[head1,head2, head3, head4, head5, head6, head7, head8]
    index=[head1,head2,head3,head4,head5,head6,head7,head8]
    mergefield=['OIDN','geometry','UIDN','TAG','EVAL','EENH1','EENH2','EENH3','EENH4','EENH5','EENH6','EENH7','PHAB5','EENH8','V1','V2','V3','HERK','INFO','BWKLABEL','HAB1','PHAB1','HAB2','PHAB2','HAB3','PHAB3','HAB4','PHAB4','HAB5','PHAB5',
    'HERKHAB','HERKPHAB','HABLEGENDE','LENGTE','OPPERVL','desc_']

    merge1=pd.merge(index[0],index[1], on=(mergefield)).merge(index[2],on=mergefield).merge(index[3],on=mergefield).merge(index[4],on=mergefield).merge(index[5],on=mergefield).merge(index[6],on=mergefield).merge(index[7],on=mergefield)
    merge1['area']=merge1['geometry'].area
    merge1['area percentage']=(merge1['area']/merge1['area'].sum())*100

    merge1['final']=merge1[['EENH1', 'EENH2', 'EENH3', 'EENH4', 'EENH5','EENH6', 'EENH7', 'EENH8']].apply(lambda x: None if x.isnull().all() else ' '.join(x.dropna()), axis=1)
    
    merge1['English_descriptions']=merge1[['eng1','eng2','eng3','eng4','eng5','eng6','eng7','eng8']].apply(lambda x: None if x.isnull().all() else ' '.join(x.dropna()), axis=1)

    
 
    return(merge1)




def shannon(lc):
    ind=[]
    a=lc['EENH1']
    value=a.value_counts()
    for v in value:
        #print(v)
        pi=v/sum(value)
   
        ln_pi=np.log(pi)
    
        mul=-(pi*ln_pi)
        #print('(pi is :%f , log pi is :%f, multiply of pi and log pi is: %f)' %(pi,ln_pi, mul))
        ind.append(mul)
   
    shanon=np.sum(ind)
    print(shanon)
    return shanon    

clips=[]
name=['DBE','OP','AS','RD','HB','MJ','DB','SG','KH']
j=0
#file_name=["C:/Users/Dell/Downloads/Testhiwi/clip1.csv","C:/Users/Dell/Downloads/Testhiwi/clip2.csv","C:/Users/Dell/Downloads/Testhiwi/clip3.csv","C:/Users/Dell/Downloads/Testhiwi/clip4.csv","C:/Users/Dell/Downloads/Testhiwi/clip5.csv","C:/Users/Dell/Downloads/Testhiwi/clip6.csv","C:/Users/Dell/Downloads/Testhiwi/clip7.csv","C:/Users/Dell/Downloads/Testhiwi/clip8.csv","C:/Users/Dell/Downloads/Testhiwi/clip9.csv"]
shanon=[np.zeros(len(name),dtype = float)]
#shapefile_name=["C:/Users/Dell/Downloads/Testhiwi/clip1.shp","C:/Users/Dell/Downloads/Testhiwi/clip2.shp","C:/Users/Dell/Downloads/Testhiwi/clip3.shp","C:/Users/Dell/Downloads/Testhiwi/clip4.shp","C:/Users/Dell/Downloads/Testhiwi/clip5.shp","C:/Users/Dell/Downloads/Testhiwi/clip6.shp","C:/Users/Dell/Downloads/Testhiwi/clip7.shp","C:/Users/Dell/Downloads/Testhiwi/clip8.shp","C:/Users/Dell/Downloads/Testhiwi/clip9.shp"]
path=("C:/Users/Dell/Downloads/Testhiwi/")

for i in buffer:
   clips=lc_utm.clip(i)
   shapefile="D:\\work\\hiwi\\germanyhiwi\\final\\Belguim\\500 meter buffer\\Shapefiles\\"+ name[j]+".shp"
   print(shapefile)
   clipss = clips.to_crs({'init': 'epsg:4326'})
   clipss.to_file(shapefile)
   filename="D:\\work\\hiwi\\germanyhiwi\\final\\Belguim\\500 meter buffer\\Excel files\\"+name[j]+".csv"
   print(filename)
   clipped=join(clipss)
   print(clipped)
   shanon.insert(j,shannon(clipped))
   #sim[j]=simpson(clipped)
 
  
   clipped.to_csv(filename,columns = ['OIDN','EVAL','EENH1','EENH2','EENH3','EENH4','EENH5','EENH6','EENH7','EENH8','area','area percentage','geometry','final','English_descriptions'])
   j+=1 
    
print(shanon)
shan=pd.DataFrame(shanon)
shan.to_excel("D:\\work\\hiwi\\germanyhiwi\\final\\Belguim\\500 meter buffer\\shannon500buffer.xlsx")


# In[ ]:




