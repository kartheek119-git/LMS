#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download the necessary NLTK data for tokenization
nltk.download('punkt')

# Sample paragraph
text = """
Natural Language Processing (NLP) is an exciting field of Artificial Intelligence.
It involves enabling computers to understand, interpret, and generate human language.
Tokenization is one of the key tasks in NLP, which involves splitting text into words and sentences.
"""

# Tokenize the paragraph into sentences
sentences = sent_tokenize(text)

# Tokenize the paragraph into words
words = word_tokenize(text)

# Print the results
print("Tokenized Sentences:")
print(sentences)
print("\nTokenized Words:")
print(words)

