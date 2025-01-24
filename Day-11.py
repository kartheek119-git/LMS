#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python script to fetch and print the title of a webpage using the 'requests' and 'BeautifulSoup' libraries. Test it with the URL: 'https://example.com'.
import requests
from bs4 import BeautifulSoup

def fetch_webpage_title(url):
    """
    Fetches and prints the title of a webpage.

    Args:
        url (str): The URL of the webpage.

    Returns:
        str: The title of the webpage.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return title
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
url = 'https://example.com'
webpage_title = fetch_webpage_title(url)
print(f"Webpage Title: {webpage_title}")

