#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[31]:


data1=pd.read_csv('D:/gapminder-FiveYearData.csv')


# In[32]:


data1


# In[33]:


data1.head()


# In[34]:


print(data1.shape)


# In[35]:


data1.columns


# In[36]:


data1.dtypes


# In[37]:


data1.info()


# In[38]:


country_data=data1['country']
country_data.head()


# In[39]:


country_data.tail()


# In[40]:


subset=data1[['country','continent','year']]
subset.head()


# In[41]:


subset.tail()


# In[42]:


data1.describe(include='all')


# In[43]:


data1.hist(figsize=(10,5))


# In[44]:


sns.boxplot(x="year",y="lifeExp",data=data1)


# In[45]:


data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[46]:


data1=data1.rename(columns={"country":"countreies"})
data1.head(5)


# In[48]:


duplicate_rows=data1[data1.duplicated()]
print('number of dupliate rows:',duplicate_rows.shape)


# In[49]:


data1.count()


# In[ ]:




