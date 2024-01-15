#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
r = int(input("Enter the radius: "))
a = (22/7)*(r**2)
print("Area of Circle is ",a)


# In[2]:


#2
name = input("Enter the name:")
rno = input("Enter the roll number:")
mark = input("Enter the mark:")
print("Name:",name)
print("Roll No:",rno)
print("Mark:",mark)


# In[18]:


#3
largest = None
while True :
    num = input("Enter the values: ")
    if num.lower() == "done":
            break
    try:
        nos = int(num)
        if largest is None or nos > largest:
            largest = nos
    except:
         print("Invalid Input")
         continue
print("The largest number is",largest)                


# In[23]:


#4
count = 0
sum = 0
for i in range(1,11):
    sum = (i-1) + i
    print("Current Number:",i)
    print("Previous Number:",i-1)
    print("Sum:",sum)


# In[1]:


#5
op = list()
while True:
    num=input("Sample Input:")
    try:
        if num.lower() == "done":
            break
        nos = int(num)
        if nos%5 == 0:
            op.append(nos)
    except:
        print("Invalid Input")
        continue
print(op) 


# In[2]:


#6
num=input("Enter a number:")
count=0
try:
    x=int(num)
    for i in range(2,100):
        if x%i==0:
            count=count+1
        else:
            continue
    if count==1:
        print(x,"is a prime number")
    else:
        print(x,"is not a prime number")
except:
    print("Invalid Input")


# In[3]:


#7
lst_1=list()
lst_2=list()
while True:
    x=input("Input:")
    try:
        if x=="done":
            break
        y=int(x)
        print(y)
        lst_1.append(y)
        
    except:
        print("Invalid Input")
        continue
print(lst_1)
for i in lst_1:
        lst_2.append(i)
lst_2.reverse()   
print(lst_2)
    
    
        
        


# In[12]:


#8
s="*"
for i in range(1,5):
    print(s*i)


# In[4]:


#9
lst=list()
y=-1
while True:
    num=input("Input:")
    x=int(num)
    lst.append(x)
    if len(lst)==3:
        break
for i in lst:
    if i>y:
        y=i
    else:
        continue
print(y)    


# In[16]:


#10
s="*"
for i in range(1,10):
    for j in range(1,6):
        if i==6:
            i=4
        elif i==7:
            i=3
        elif i==8:
            i=2
        elif i==9:
            i=1
        print(s*j*i)
        break
    continue    

