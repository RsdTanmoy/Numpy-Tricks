#!/usr/bin/env python
# coding: utf-8

# # n-d Array

# In[4]:


#1-D array
import numpy as np
a = np.array([1,2,3])
print(a)


# In[5]:


#2-D array
import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print(b)


# In[6]:


b


# In[8]:


b[0] #1st row


# In[9]:


b[1] #2nd row


# In[12]:


print(type(a))
print(type(b))


# In[ ]:





# # Initializing Numpy array

# In[13]:


import numpy as np
np.zeros((3,4))
#np.zeros((row,column))


# In[ ]:





# Arranging the numbers between x and y with an interval

# In[16]:


import numpy as np
#np.arange(1st value,last value, interval)
np.arange(10,25,5)


# In[17]:


import numpy as np
np.arange(10,30,3)


# In[18]:


import numpy as np
np.arange(10,20,2)


# In[ ]:





# Arranging 'z' numbers between x and y

# In[19]:


import numpy as np
np.linspace(5,10,5)


# In[20]:


import numpy as np
np.linspace(0,10,10)


# In[21]:


import numpy as np
np.linspace(0,10,6)


# In[ ]:





# Filling same number in a array 

# In[23]:


import numpy as np
#np.full((row,column),number)
np.full((3,4),5)


# In[24]:


import numpy as np
#np.full((row,column),number)
np.full((2,4),6)


# In[ ]:





# Filling random number in a array

# In[26]:


import numpy as np
#np.random.random((row,column))
np.random.random((2,4))


# In[27]:


import numpy as np
#np.random.random((row,column))
np.random.random((3,3))


# In[ ]:





# # Numpy array dimensions

# In[28]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.shape)


# In[29]:


import numpy as np
a=np.array([[1,2,3,5],[4,4,5,6],[6,7,8,9]])
print(a)
print(a.shape)


# In[30]:


a= np.array([[1,2,3],[4,5,6]])


# In[32]:


print(a)
print(a.shape)


# In[44]:


a.shape=(3,2)
print(a)
print(a[1]) #2nd row
print(a.shape[0]) #shows the row number 
print(a.shape[1]) #shows the column number 


# In[ ]:





# Array arrange number

# In[45]:


import numpy as np
a=np.arange(24)

print(a.size)
print(a)


# In[ ]:





# Dimensions

# In[51]:


a=np.array([[1,2,3],[4,5,6]])
a.shape=(3,2)
print(a)
#number of dimensions of the array
print(a.ndim)


# In[ ]:





# Returns datatype of an array

# In[62]:


import numpy as np
a= np.arange(24,dtype=float)
print(a)
print(a.size)
print(a.ndim)
print(a.dtype)

b=a.reshape(3,4,2)
print(b)


# In[ ]:





# # Array Mathematics

# In[64]:


import numpy as np
a,b=10,20
np.sum([a,b])


# In[72]:


a=[5,10]
b=[2,3]

np.subtract(a,b)


# In[ ]:





# In[70]:


a=np.array([[0,1],[0,5]])
print(a)

# axis =0 columnwise sum
b=np.sum(a,axis=0)
print(b)

# axis =1 rowwise sum
c=np.sum(a,axis=1)
print(c)


# In[74]:


a=[5,10]
b=[2,3]

print(a)
print(b)


# In[75]:


np.divide(a,b)


# In[76]:


np.multiply(a,b)


# In[77]:


np.exp(a)


# In[78]:


np.sqrt(b)


# In[79]:


np.sin(a)


# In[80]:


np.cos(b)


# In[81]:


np.log(a)


# In[ ]:





# Element-wise comparison

# In[83]:


import numpy as np
a=[1,2,4]
b=[2,3,4]
c=[1,2,4]

print(np.equal(a,b))
print(np.equal(a,c))
print(np.equal(b,c))


# In[ ]:





# Array-wise comparison

# In[84]:


import numpy as np
a=[1,2,4]
b=[2,3,4]
c=[1,2,4]

print(np.array_equal(a,b))
print(np.array_equal(a,c))
print(np.array_equal(b,c))


# In[ ]:





# Aggregate Functions

# In[86]:


import numpy as np
a=[1,2,4]
b=[2,3,4]
c=[1,2,4]

print(np.sum(a))
print(np.min(a))
print(np.mean(a))
print(np.median(a))
print(np.corrcoef(a))
print(np.std(a))


# In[ ]:





# # Numpy Array Broadcasting

# In[87]:


import numpy as np

a= np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
b=np.array([0,1,2])

print('First array:\n',a,'\n')
print('Second array:\n',b,'\n')
print('Broadcasting array:\n',a+b,'\n')


# In[ ]:





# Indexing and Slicing in Numpy Array

# In[9]:


# simple indexing
import numpy as np
a = np.array([11, 22, 33, 44, 55])

# index data
print(a)
print(a[0])
print(a[4])


# In[13]:


# 2d indexing
import numpy as np
# define array
a = np.array([[11, 22], [33, 44], [55, 66]])
# index data
print(a)
print(a[0,0])
print(a[0,])
print(a[0,1])
print(a[2,0])


# In[63]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Full array:\n',a,'\n')
print('Row Slicing:\n')
print('1st Row Slicing:\n',a[0])
print('2nd Row Slicing:\n',a[1])
print('3rd Row Slicing:\n',a[2],'\n')

print('1st Row Slicing in list:\n',a[:1],'\n')
print('1st Row all element Slicing in list:\n',a[:1,:],'\n')
print('1st Row 1st element Slicing in list:\n',a[:1,:1],'\n')
print('1st Row last two element Slicing in list:\n',a[:1,1:],'\n')

print('1st column Slicing in list:\n',a[:,:1],'\n')
print('2nd column Slicing in list:\n',a[:,1:2],'\n')
print('3rd column Slicing in list:\n',a[:,2:3],'\n')

#Here a[row:,:column]
print('2nd row- 2nd column middle element Slicing:\n',a[1:2,1:2],'\n')
print('3nd row- 3nd column last element Slicing:\n',a[2:3,2:3],'\n')


# In[ ]:





# # Array Manipulation

# Array Concatenation

# In[65]:


import numpy as np
a=np.array([1,2,3])
b=np.array([3,4,5])


# In[69]:


np.concatenate([a,b],axis=0)


# In[82]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[3,4,5],[5,6,7]])

print('First array:\n',a,'\n')
print('Second array:\n',b,'\n')

print('row wise concate array:')
print(np.concatenate([a,b],axis=0),'\n')

print('column wise concate array:')
print(np.concatenate([a,b],axis=1),'\n')


# In[ ]:





# Array Stacking

# In[99]:


import numpy as np
a=np.array([1,2,3])
b=np.array([3,4,5])
print('First array:',a)
print('Second array:',b,'\n')
print('Horizontal Stack:\n',np.hstack((a,b)),'\n')
print('Vertical Stack:\n',np.vstack((a,b)),'\n')


# In[ ]:





# In[104]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[3,4,5],[5,6,7]])

print('First array:\n',a,'\n')
print('Second array:\n',b,'\n')

#Here Horizontal concate is equal to vertical stack
# vertical concate = horizontal stack = column stack 

print('Horizontal Stack:\n',np.hstack((a,b)),'\n')
print('Horizontal concate:')
print(np.concatenate([a,b],axis=0),'\n')

print('Vertical Stack:\n',np.vstack((a,b)),'\n')
print('Vertical concate:')
print(np.concatenate([a,b],axis=1),'\n')

print('Column Stack:')
print(np.column_stack((a,b)),'\n')


# In[ ]:





# Splitting Arrays

# In[116]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])

print(a,'\n')
print('Split 2 array in row:')
print(np.split(a,2,axis=0),'\n')

print('Split 3 array in column:')
print(np.split(a,3,axis=1))


# In[ ]:





# In[124]:


import numpy as np 
a = np.arange(9) 

print('First array:') 
print (a,'\n') 
  

print ('Split the array in 3 equal-sized subarrays:') 
b = np.split(a,3) 
print (b,'\n')  

print('Split the array at positions indicated in 1-D array:') 
b = np.split(a,[4,7])
print (b,'\n') 


print('Split the array at positions indicated in 1-D array:') 
c = np.split(a,[3,5,10])
print (c) 


# In[ ]:





# In[123]:


x = np.arange(8.0)
np.split(x, [3, 5, 6, 10])


# In[ ]:





# In[ ]:




