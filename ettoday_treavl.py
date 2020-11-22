import requests
from bs4 import BeautifulSoup

for i in range(1,4):
    print("第%d頁..."%i)
    url='https://travel.ettoday.net/category/綠島/?&page='+str(i)
    html=requests.get(url)
    soup=BeautifulSoup(html.text, 'html.parser')
    t=soup.find_all('h3', itemprop='headline')
    for i in t:
        title=i.find('a')
        url=i.a['href']
        print(title.getText())
        if url.startswith('https://'):
            print(url)
