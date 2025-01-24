#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function to clean a given text by removing special characters and converting it to lowercase. Test it with the input: 'Hello, World! Welcome to NLP 101.'
import re
def clean_text(text):
    """
    Cleans the input text by:
    1. Removing special characters and punctuation.
    2. Converting the text to lowercase.
    
    Args:
        text (str): The input text to be cleaned.
    
    Returns:
        str: The cleaned text.
    """
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    cleaned_text = cleaned_text.lower()
    return cleaned_text
input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_text = clean_text(input_text)
print("Original Text:", input_text)
print("Cleaned Text:", cleaned_text)

