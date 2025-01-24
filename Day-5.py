#!/usr/bin/env python
# coding: utf-8

# In[1]:


#5. Write a Python program to calculate the frequency of each word in a given text. Print thewords and their corresponding counts
text = input("Enter a text: ").lower()
word_frequency = {}
for word in text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("\nWord Frequencies:", word_frequency)

