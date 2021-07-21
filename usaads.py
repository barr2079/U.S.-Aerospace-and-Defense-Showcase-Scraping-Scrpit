#!/usr/bin/env python
# coding: utf-8

# In[5]:


# setup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import chromedriver_binary


# In[6]:


# set variables
username = "hyzhgaivjcylqfthpt@rffff.net"
password ="ZLHDCv3TT9vpkPz"
URL1="https://www.usaaerodefshowcase.com/login?snc=668648&destination=node%2F668648&snc=668648&rel=nofollow"
URL = "https://www.usaaerodefshowcase.com/#hallfilter=271194_320257_All.&lct=exhibithall"


# In[7]:


# open URL in Chrome


driver = webdriver.Chrome()


#driver.maximize_window()
driver.implicitly_wait(10)
actions = ActionChains(driver)
driver.get(URL)
driver.find_element_by_id("edit-name").send_keys(username)

driver.find_element_by_id("edit-pass").send_keys(password)

driver.find_element_by_id("edit-submit").click()
# driver.get(URL1)
time.sleep(20) 


# In[8]:


content = driver.page_source
soup = BeautifulSoup(content,)

table = soup.find('div', id = 'mCSB_2')
cards = table.find_all('li')

links = []

for card in cards:
    a = card.find('a')
    if a != None:
        link = a['href']
    else:
        link = None
        name = None
    links.append(link)

print(links)


# In[ ]:


content = driver.page_source
soup = BeautifulSoup(content)

table = soup.find('div', id = 'mCSB_2')
cards = table.find_all('li')

names = []

for card in cards:
    name = card.find('td', class_ = 'exhibit-title')
    if name != None:
        name = name.find('div').text
    names.append(name)
    
print(names)


# In[ ]:


exhibitors_df = pd.DataFrame({'Name':names, 'Link':links})


# In[ ]:


# write csv
csv = "usaaerodef_exhibitors.csv"
exhibitors_df.to_csv(csv)


# In[ ]:




