import requests
from bs4 import BeautifulSoup
import os, time

class panda_sounds(object):
    def __init__(self):
        self.url='https://www.tukuppt.com/yinxiaomuban/zhuanchang/__zonghe_0_0_0_0_0_0_%7B%7D.html'

    def exPath(self, destpath, i):
        if not os.path.exists(destpath):
            os.mkdir(destpath)
        filename=os.path.basename(i)
        with open(os.path.join(destpath, filename), 'w') as df:
            df.write(i)
            print("%s下載成功..."%filename)
            time.sleep(1)
        df.close()
    def getHtml(self, destpath):
        html=requests.get(self.url)
        soup=BeautifulSoup(html.text, 'lxml')
        box=soup.find('div', 'b-box')
        dl=box.find_all('dl')
        for a in dl:
            audio=a.find('audio')
            source=audio.find('source')['src']
            allUrl="http:"+source
            self.exPath(destpath, allUrl)
        return allUrl

if __name__=='__main__':
    destpath=r'D:\暫存\panda_office'
    pd=panda_sounds()
    pd.getHtml(destpath)