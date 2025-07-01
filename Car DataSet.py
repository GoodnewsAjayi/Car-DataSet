#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


car = pd.read_csv (r"C:\Users\oodan\Downloads\Project+2+-+Cars+Dataset.csv")


# In[75]:


car


# In[76]:


car.head(50)


# In[77]:


car.shape


# In[82]:


car.isnull().sum()


# In[83]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)


# In[84]:


car.isnull().sum()


# In[85]:


car['EngineSize'].fillna(car['EngineSize'].mean(), inplace = True)


# In[48]:


car.isnull().sum()


# In[87]:


car['Horsepower'].fillna(car['Horsepower'].mean(), inplace = True)


# In[86]:


car.isnull().sum()


# In[56]:


car['Length'].fillna(car['Length'].mean(), inplace = True)


# In[57]:


car['Wheelbase'].fillna(car['Wheelbase'].mean(), inplace = True)


# In[59]:


car['Weight'].fillna(car['Weight'].mean(), inplace = True)


# In[65]:


car['MPG_City'].fillna(car['MPG_City'].mean(), inplace = True)


# In[89]:


car.isnull().sum()


# In[94]:


car.count()


# In[95]:


car.head(2)


# In[99]:


car.value_counts()


# In[100]:


car.head(2)


# In[101]:


car['Make'].value_counts()


# In[103]:


car.head(2)


# In[105]:


car[car['Origin'] == 'Asia']


# In[107]:


car[car['Origin'] == 'Europe']


# In[114]:


car[(car['Origin'] == 'Asia') | (car['Origin'] == 'Europe')]


# In[5]:


car.head(2)


# In[7]:


car[car['Weight']> 4000]


# In[10]:


car[~(car['Weight']> 4000)]


# In[11]:


car.head(2)


# In[17]:


car['MPG_City'] = car['MPG_City'].apply(lambda x: x + 3)


# In[21]:


car.head(2)


# In[ ]:




