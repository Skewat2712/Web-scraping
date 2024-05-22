#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Amazon Customer Reviews from Amazon website
import requests 
from bs4 import BeautifulSoup as bs


# In[13]:


url = 'https://www.amazon.in/Samsung-Galaxy-Ultra-Phantom-Storage/product-reviews/B0BT9FDZ8N/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(url) #Requesting the contents of the above url
page


# In[14]:


page.content


# In[15]:


soup = bs(page.content,'html.parser')
soup


# In[16]:


names = soup.find_all('span',class_ = 'a-profile-name')[2:]
names


# In[18]:


import pandas as pd 
df = pd.DataFrame(names,columns = ['Customer Name'])
df


# In[19]:


len(names)


# In[28]:


df = df.drop_duplicates(ignore_index = True)
df


# In[29]:


r_title = soup.find_all('a',class_ = 'review-title')
r_title


# In[30]:


len(r_title)


# In[48]:


#Data Cleaning/Filtering
review_title = [] #empty list

#for i in range(0,10):
for i in range(0,len(r_title)):
  review_title.append(r_title[i].get_text()[1:-1].replace('.0 out of 5 stars\n',' '))
review_title


# In[49]:


dates = soup.find_all('span',class_ = 'review-date')[2:]
dates


# In[50]:


len(dates)


# In[51]:


#Data Cleaning
review_date = [] #empty list
for i in range(0,len(dates)):
  review_date.append(dates[i].get_text().replace('Reviewed in India 🇮🇳 on ',''))
review_date


# In[52]:


rating = soup.find_all('i',class_ = 'review-rating')[2:]
rating


# In[53]:


len(rating)


# In[54]:


review_rating = [] #empty list
for i in range(0,len(rating)):
  review_rating.append(rating[i].get_text())
review_rating


# In[55]:


content = soup.find_all('span',class_ = 'review-text-content')
content


# In[56]:


len(content)


# In[57]:


review_content = []
for i in range(0,len(content)):
  review_content.append(content[i].get_text().replace('\n',''))
review_content


# In[58]:


df['Review title'] = review_title
df['Review date'] = review_date
df['Review rating'] = review_rating
df['Review content'] = review_content
df


# In[61]:


df.to_csv('CUSTOMER_REVIEW_SMARTPHONE.csv')


# In[ ]:




