#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1
inp = input("Enter a string value: ")
lst1 = list()
for i in inp:
        lst1.append(i)
for i in lst1:
    print(i,lst1.count(i))
        


# In[1]:


#2
lst = list()
while True:
    try:
        num = int(input("Input:"))
        lst.append(num)
        if len(lst) == 3:
            print(max(lst))
            break
    except:
        print("Invalid Input")


# In[2]:


#3
def exponent(base,exp):
    return(base**exp)
inp1 = int(input("Enter the base: "))
inp2 = int(input("Enter the exponent: "))
exponent(inp1,inp2)


# In[3]:


#4
def inp(n):
    out=0
    for i in range(n):
        out=out+i**3
    return(out)
m = int(input("Sample input: "))
inp(m)


# In[4]:


#5
for i in range(1,11):
    if i%2==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%2==0:
        print("Fizz")
    else:
        print(i)


# In[10]:


#6
lst = list()
while True:
    inp = input("Enter a number:")
    if inp == "done":
        break
    else:
        num = int(inp)
        lst.append(num)
for i in lst:
    c = lst.count(i)
    print(i,c)

    


        
    


# In[6]:


#7
lst = list()
sum = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    else:
        num = int(inp)
        lst.append(num)
for i in lst:
    sum = sum+i**2
print(sum)    


# In[8]:


#8
for i in range(1,16):
    if i%2!=0:
        print(i,"-","odd")
    else:
        print(i,"-","even")


# In[12]:


#9
f = int(input("Temperature in Fahrenheit = "))
c = 5*(f-32)/9
print("Temperature in Celsius =",c)


# In[17]:


#10
total = 1
num = int(input("Enter a number: "))
for i in range(1,num+1):
    total = total*i
print(total)    


# In[ ]:




