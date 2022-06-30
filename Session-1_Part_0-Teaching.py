#!/usr/bin/env python
# coding: utf-8

# # Numpy vs Lists 

# In[1]:


#Let's define a list in python.
heights = [74, 75, 72, 72, 71]


# In[2]:


weights = [55, 60, 65, 70, 75,]


# In[3]:


weights


# In[3]:


# Print the heights.
heights


# In[6]:


# Try to multiple heights with a scalar.
heights * 2.54


# In[4]:


import numpy as np


# In[5]:


# Deine a NumPy array
np_heights = np.array([74, 75, 72, 72, 71])


# In[6]:


np_weights = np.array(weights)


# In[8]:


np_weights_pounds = np_weights*2.20


# In[10]:


np_weights_pounds


# In[11]:


# print the type of Numpy array.
type(np_weights_pounds)


# In[10]:


np_heights


# In[11]:


# Print the type of a NumPy array.
type(np_heights)


# In[12]:


# Multiple height (NumPy array) with a scalar.
np_heights * 2.54


# In[ ]:





# 
# #### NumPy comes with its own set of methods and operations

# In[40]:


# Let's define two lists and perform '+' operation on that.
list_1 = [1,2,3]
list_2 = [4,5,6]
list_1 + list_2


# In[14]:


list_3 = [7,8,9]
list_4 = [3,2,1]
list_3 + list_4


# In[27]:


np_list_3 = np.array([7,8,9])
np_list_4 = np.array([3,2,1])
np_list_3 + np_list_4


# In[21]:


np_list


# In[41]:


# Let's define two NumPy array and perform '+' operation on that.
np1 = np.array([1,2,3])
np2 = np.array([4,5,6])
np1 + np2


# #### Working with N-D Arrays

# In[45]:


np_heights


# In[46]:


type(np_heights)


# In[ ]:





# In[33]:


l1=np.array( [1.0, 2, 3.5, 0.2, True])


# In[37]:


type(l1)


# In[ ]:




