#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function using regular expressions to extract all email addresses from a given string. Test it with the input: 'Contact us at support@example.com and sales@example.org.'
import re
def extract_emails(text):
    """
    Extracts all email addresses from the given text using a regular expression.

    Args:
        text (str): The input text to search for email addresses.

    Returns:
        list: A list of extracted email addresses.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails
input_text = 'Contact us at support@example.com and sales@example.org.'
extracted_emails = extract_emails(input_text)
print("Extracted Emails:", extracted_emails)

