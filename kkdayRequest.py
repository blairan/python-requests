import requests
from pprint import pprint
import csv

class kkday():
    """
    爬取kkday旅遊票券
    """
    def __init__(self, cityName, page):
        self.cityName=cityName
        self.page=page
    def getData(self):
        
        result=[]
        if self.cityName:
            for i in range(1,self.page):#要查找的頁數
                url='https://m.kkday.com/zh-tw/product/ajax_get_productlist?page='+str(i)+'&keyword='+\
                    str(self.cityName)+'&sort=rdesc'
                response=requests.get(url)
                activities = response.json()["data"]["productlist"]#轉成json檔
                for activtie in activities:#找出json裡想要存檔的資訊
                    title=activtie["name"]
                    price=activtie["display_price"]
                    date=activtie['earliest_sale_date']
                    star=activtie['rating_count']
                    url=activtie["url"]
                    #以字典的型態加入列表裡
                    result.append({'標題':title, 
                                    '價格(元)':price, 
                                    '日期':date, 
                                    '評價':star, 
                                    '連結':url
                                })
        keys=result[0].keys()#抽取字典裡的key{'key':value}
        #存成csv
        with open('kkday一日遊票券.csv', 'w', newline='', encoding='utf-8-sig') as f:
            dw=csv.DictWriter(f, keys)
            dw.writeheader()
            dw.writerows(result)

        return result
cityname=input("輸人想查找的城市: ")
page=eval(input("輸入想爬取的頁數:"))      
kkdayR=kkday(cityname, page)
pprint(kkdayR.getData())




