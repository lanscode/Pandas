
# coding: utf-8

# ## myfirst tutorial of pandas library

# In[61]:


#libraries import
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import matplotlib
#enable inline plotting
get_ipython().magic('matplotlib inline')

print('python version is:'+sys.version)
print('pandas version is :'+pd.__version__)
print('matplotlib version is:'+matplotlib.__version__) 

names=['Bob','Jessica','Laila','Boutayna','Mel']
births=[968,155,77,578,973]
#we wil merge these two list in list using zip
babyDataSet=list(zip(names,births))
df = pd.DataFrame(data=babyDataSet,columns=['Names','Births'])

df.to_csv('C:\\Users\\koria\\Desktop\\coursS5\\DataScience\\births1880.csv',index=False,header=True)
datas=r'C:\\Users\\koria\\Desktop\\coursS5\\DataScience\\births1880.csv'
#dataUser=r'C:\\Users\\koria\\births1880.csv'

#i delete the first file i created on my disk
#os.remove(dataUser)

df=pd.read_csv(datas)
print(df.dtypes)
print('----------------------------------------------------------')
print(df)

print('\n')




# In[91]:


#Here w're going to find the highest values of births
#method 1
sorted_data=df.sort_values(['Births'],ascending=False)
print(sorted_data.head(1))
# Create graph
df['Births'].plot()
# Maximum value in the data set
maxValue = df['Births'].max()

# Name associated with the maximum value
maxName = df['Names'][df['Births'] == maxValue].values
plt.annotate(maxName[0],xytext=(5,1208),xy=(0.01,maxValue),arrowprops=dict(facecolor='black', shrink=0.02),)

print("The most popular name:"+maxName[0])
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used

