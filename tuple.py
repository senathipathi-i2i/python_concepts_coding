#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tuple concepts and example

tuple_name = ('sethu','yechu','surya','babu','babu')
tuple_name


# In[2]:


#lenth
tuple_name = ('sethu','yechu','surya','babu','babu')
print(len(tuple_name))


# In[3]:


#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("sethu",)
print(type(thistuple))

#NOT a tuple
thistuple = ("sethu")
print(type(thistuple))


# In[4]:


#accesing diffrent data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)


# In[5]:


#negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# In[6]:


#doest mandotary to open to close paranthesis 
k = 2,3,5,2,7
print(type(k))


# In[7]:


tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[:4])


# In[8]:


tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[4:])


# In[9]:


tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[-4:])


# In[10]:


tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[:-4])


# In[15]:


#adding the tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple = thistuple + y
print(thistuple)


# In[16]:


#packing and unpacking
fruits = ("apple", "banana", "cherry")
fruits


# In[17]:


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# In[22]:


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, red, purple, *orange) = fruits

print(green)
print(yellow)
print(orange)


# In[25]:


#loop through a tuple
tuple_item= ("apple", "banana", "cherry")
for i in range(len(tuple_item)):
    print(tuple_item[i])


# In[34]:


this_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(this_tuple):
    print(this_tuple[i])
    i = i + 1


# In[35]:


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# In[36]:


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# In[3]:


tuple_name = ('sethu','yechu','surya','babu','babu')
print(max(tuple_name))


# In[7]:


for i in range(1, 10, 5):
    print(i)
