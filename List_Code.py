
#!/usr/bin/env python
# coding: utf-8

# In[7]:


# list using some example
#creating list
list_1 = ['sethu','yechu','surya','babu']
list_1


# In[10]:


#list allowing duplicate
list_1 = ['sethu','yechu','surya','babu','babu']
print(list_1)
print(len(list_1))


# In[12]:


#list contain multiple data types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


# In[1]:


list1 = ["abc", 34, True, 40, "male"]


# In[18]:


#python accessing item using indexing
list_1 = ['sethu','yechu','surya','babu']
print(list_1[0])
print(list_1[-1])
print(list_1[-2])


# In[26]:


#range of indexes
list = ['sethu','yechu','surya','babu','babu','chandru','chandru']
print(list_1[1:5])
print(list_1[2:6])
# firt four names
print(list_1[:4])
# include bubu but not chandru
print(list_1[-4:-1])


# In[61]:


#list using if condition
list_1 = ['sethu','yechu','surya','babu','babu','chandru','chandru']
if "babu" in list_1:
    print("Yes, 'babu' is in the given list")


# In[28]:


#changing the list value
list_1 = ['sethu','yechu','surya','babu','babu','chandru','chandru']
list_1[3] = 'david'
print(list_1)


# In[40]:


#inserting range value
list_1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list_1[1:4] = ["parthi", "siva"]
print(list_1)


# In[41]:


#adding item in list
list_1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list_1.insert(2, "watson")
print(list_1)


# In[42]:


#appending
list_1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list_1.append("watson")
list_1


# In[47]:


#Remove Specified Item
list_1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list_1.remove('surya')
print(list)
#Remove Specified Index
list_1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list_1.pop(3)
print(list_1)


# In[53]:


#using del keyword to remove
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
del list1[0]
print(list1)


# In[52]:


#entire list deleting
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
del list1
print(list1)


# In[54]:


#clearing entire list
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list1.clear()
print(list1)


# In[57]:


#loop through a list
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
for x in list1:
    print(x)


# In[58]:


#Loop Through the Index Numbers
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
for i in range(len(list1)):
    print(list1[i])


# In[60]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


# In[62]:


#list sorting
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort()
print(list1)


# In[63]:


list1 = [45,2,4432,4352,54]
list1.sort()
list1


# In[66]:


#decending
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list1.sort(reverse = True)
print(list1)


# In[67]:


list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list1.sort(reverse = False)
print(list1)


# In[69]:


list1 = ["banana", "Orange", "Kiwi", "cherry"]
list1.sort()
print(list1)


# In[73]:


list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list1.reverse()
print(list1)


# In[74]:


#copy of list
list1 = ['sethu','yechu','surya','babu','barath','chandru','mani']
list1= list1.copy()
print(list1)


# In[78]:


#joining list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2

print(list3)


# In[83]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    print(list1)


# In[3]:


import sys
list1 = [1,2,'three',4]
print(sys.getsizeof(list1))


# In[3]:


k = ['hi','hello','d','d','ri','uefuieh']

for i in range(len(k)):
    print(i)


# In[40]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# In[44]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
    newlist.append(x)

print(newlist)


# In[45]:


list = ['seth','dede','dugdu']
empty_list = []

for x in list:
    if 'e' in x:
        empty_list.append(x)
print(empty_list)
        


# In[51]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# In[ ]:




