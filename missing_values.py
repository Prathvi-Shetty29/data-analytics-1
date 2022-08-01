#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv("D:\Data Analytics\employees.csv")


# In[4]:


print(df.head())


# In[5]:


print(df.dtypes)


# In[7]:


print(df.describe())


# In[9]:


print('Salary')
print(df['Salary'].head(10))


# In[10]:


print(df['Gender'].head(10))


# In[12]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("D:\Data Analytics\employees.csv",na_values=missing_value_formats)
print(df['Gender'].head(10))


# In[14]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("D:\Data Analytics\employees.csv",na_values=missing_value_formats)
def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
df['Salary']=df['Salary'].map(make_int)
print(df['Salary'].head() )


# In[15]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))


# In[16]:


null_filter=df['Gender'].notnull()
print(df[null_filter].head())


# In[17]:


print(df.isnull().values.any())


# In[18]:


print(df.isnull().sum())


# In[19]:


new_df=df.dropna(axis=0)
print(new_df.isnull().values.any())


# In[20]:


new_df=df.dropna(axis =0,how='any')
new_df=df.dropna(axis =0,how='all')
new_df=df.dropna(axis =1,how='any')
new_df=df.dropna(axis =0,how='all')


# In[22]:


df['Salary'].fillna(0)


# In[23]:


df['Gender'].fillna('No Gender')


# In[24]:


df['Salary'].fillna(method='pad')


# In[25]:


df['Salary'].fillna(method='bfill')


# In[27]:


df['Salary'].fillna(df['Salary'].median())


# In[29]:


df['Salary'].fillna(df['Salary'].mean())


# In[31]:


df['Salary'].replace(to_replace=np.nan,value=0)


# In[32]:


df['Salary'].interpolate(method='linear',direction='forward')


# In[ ]:




