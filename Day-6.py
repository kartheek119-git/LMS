#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Write a Python program to using NLTK and Spacy
#Convert text to lowercase.
txxt = "Hello World"
lowercase= text.lower()
print("Lowercase Text:", lowercase)


# In[1]:


#Remove stopwords using NLTK
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
text = "NLP is a Natural language process which is very useful for sentiment analysis and it has many real time projects though itd very easy to do and it is a beautiful language and it is specificially and widely used in business purposes"
words = text.split()
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = ''.join(filtered_words)
print("Filtered Text:",filtered_text)


# In[ ]:




