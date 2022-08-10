#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[3]:


x=stats.norm.rvs(30,10,30)
result=stats.ttest_1samp(x,27)
alpha=0.05
if(result[0]<0) & (result[1]/2<alpha):
    print("reject null hypothesis,mean is greater than 27")
else:
    print("accept null hypothesis")


# In[4]:


y=stats.norm.rvs(500,10,30)
res=stats.ttest_1samp(x,505)


# In[5]:


res


# In[6]:


import math
xbar=505
SEM=(10/math.sqrt(30))


# In[7]:


mu=500
z=(xbar-mu)/SEM
z


# In[8]:


pval=2*(1-stats.norm.cdf(z))
pval


# In[9]:


if (pval<alpha):
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


# In[ ]:




