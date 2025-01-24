#!/usr/bin/env python
# coding: utf-8

# In[1]:


#4.Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n
n = int(input("Enter a positive integer: "))
even_sum = 0
for i in range(2, n + 1, 2):  
    even_sum += i
print(f"The sum of all even numbers between 1 and {n} is: {even_sum}")


# In[ ]:




