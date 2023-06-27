#!/usr/bin/env python
# coding: utf-8

# # list comprehension

# In[2]:


h = []
for i in "human":
    h.append(i)
h


# In[1]:


h = [letter for letter in "human"]
h


# In[2]:


h = [x*2 for  x in range(1,11)]
h


# In[ ]:





# In[4]:


p = [x*3 for x in range(1,11)]
p


# In[5]:


k = [x*3 for x in range(1,12)]
k


# In[6]:


o = [x*4 for x in range(1,13)]
o


# In[8]:


m = [x*5 for x in range(1,15)]
m


# In[9]:


q = [x*6 for x in range(1,14)]
q


# In[11]:


l = [x*7 for x in range(1,10)]
l


# In[14]:


l = [x for x in range(1,40) if x%2==0]
l


# In[19]:


s =[x for x in range(1,25) if x%2==0]
s


# In[29]:


k = []
for x in range(1,32):
   if x%2==0:
      k.append(x)
k


# In[40]:


z = []
for x in range(1,28):
      if x%2==0:
            z.append(k)
z


# In[42]:


x = int(input("enter your value"))
h = [i*x for i in range (1,14)]
h


# In[49]:


x = int(input("enter your value"))
h = [i*x for i in range(1,10)]
h


# In[2]:


a = input("enter your name")
if(a==a[::-1]):
    print("yes it is")
else:
    print("not it is")


# In[2]:


matrix = [[1,2,3,4],[5,6,7,8]]
transpose =[]
for i in range(len(matrix[0])):
     row=[]
     for j in matrix:
            row.append(j[i])
     transpose.append(row)
transpose


# In[53]:


k = input("plese enter your name")
if (k==k[::-1]):
    print("yes your name is plandram")
else:
    print("i am really sorry your name is not a pladrome word")


# In[2]:


for i in range(10):
    print(i)



# # dictionary

# In[4]:


a ={ "ali": "74755", "kabeer": "9897"}
type(a)


# In[6]:


a = dict([(1,'a'),(2,'b'),(3,'c'),(4,'d')])
a


# In[4]:


a = {
    'a':"apple",
    'b':"carrot",
    'c': "car",
    'd': "byke"
}
a.get('b','not found')


# In[5]:


for i in a.keys():
    print(i)


# In[6]:


for i in a.values():
    print(i)


# In[7]:


for key,value in a.items():
    print(key,value)


# In[3]:


list1 = [1,2,3,4,5,6]
list2 = ['a','b','c','d','e','f','g']
res={}
# for key in list1:
#     for value in list2:
#          res[key] = value
#          list2.remove(value)
#          break
# res
res= dict(zip(list1,list2))
res


# In[2]:


a ={1:'a',2: 'b', 3: 'c'}
#pop
#clear
#del

print(a.pop(2))


# In[3]:


print(a)


# In[9]:


a = 3
b = 4
c = a+b
print(c)



def sum(a,b):
    c = a+b
    print(c)
sum(9,2)
     


# In[ ]:




