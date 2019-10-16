
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup

google_url = 'https://www.google.com.tw/search'

my_params = {'q':'我是鴨'}

r = requests.get(google_url , params = my_params )

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text , 'html.parser')
    
    print(soup.prettify())
    
    items = soup.select('div.kCrYT > a[href^="/url"]')
    
    for i in items:
        print("火爆新聞:" + i.text)
        print("火爆網址:" + i.get('href'))

