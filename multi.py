#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
arr2 = np.array([[1,2,3],[4,5,6]])
arr2


# In[8]:


print ("the shape is 2 rows and 3 columns",arr2.shape)


# In[13]:


print(arr2[0][2])
print (arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[17]:


arr3 = np.array(['india','china','usa','mexico'])
print(arr3)


# In[19]:


arr3[1]


# In[21]:


arr=np.arange(0,20,2)
print(arr)


# In[33]:


arr=np.linspace(0,10,20)
print(arr)


# In[36]:


arr=np.random.rand(10)
print(arr)


# In[27]:


arr=np.random.rand(3,4)
print(arr)


# In[34]:


print(np.full((4,6),10))


# In[39]:


arr=[0,2,1]
print(np.repeat(arr,4))


# In[40]:


arr=[0,1,2]
print(np.tile(arr,4))


# In[49]:


identity_matrix=np.eye(3)
print(identity_matrix)


# In[54]:


identity_matrix=np.identity(3)
print(identity_matrix)


# In[46]:


arr=np.random.rand(5,5)
print(arr)


# In[53]:


print(np.sum(arr,axis=0))


# In[55]:


print(np.sum(arr,axis=1))


# In[56]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[71]:


arr=np.random.rand(5,5)
print(np.sort(arr,axis=1))


# In[62]:


arr=np.array([4,5,6,7])


# In[65]:


arr1=np.append(arr,8)
print(arr1)


# In[66]:


arr2=np.append(arr,[9,10,11])
print(arr2)


# In[68]:


arr2=np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5=np.delete(arr2,[1,4])
print(arr5)


# In[82]:


arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr2=np.array([[5,6,7,8],[5,6,7,8]])


# In[76]:


cat=np.concatenate((arr1,arr2),axis=0)
print(cat)


# In[77]:


cat=np.concatenate((arr1,arr2),axis=1)
print(cat)


# In[ ]:




