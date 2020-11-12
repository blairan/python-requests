import requests
import os, time
import m3u8

##抓"小白影音"m3u8的ts檔

def downloadTS(savepath, seg):
    with open(os.path.join(savepath, seg.uri), 'wb') as d:
        d.write(tsfiles.content)
        RETURN="%s...下載完成"%seg.uri
        d.close()
    time.sleep(1)
    return RETURN

tsUrl='https://yiyi.55zuiday.com/20180216/hsMX5SId/800kb/hls/'
savepath=r'D:/暫存/test'
m3u8_url=r'https://yiyi.55zuiday.com/20180216/hsMX5SId/800kb/hls/index.m3u8'
m3u8_obj=m3u8.load(m3u8_url)
for seg in m3u8_obj.segments:
    dest_url=tsUrl+seg.uri
    print(dest_url)

    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
                Safari/537.36', }
    tsfiles=requests.get(dest_url, headers=headers)
    if tsfiles.status_code==200:
        print(tsfiles,dest_url)
    print(downloadTS(savepath, seg))


##############################################################################

#參考 https://blog.csdn.net/human_soul/article/details/103263573

解析m3u8并提取url
一、安装m3u8库

pip install m3u8
cryptor = AES.new(key, AES.MODE_CBC, key)
1
2
二、解析提取url

import m3u8

m3u8_obj = m3u8.load(r'C:\Users\Administrator\Desktop\anylise\hls-720p.m3u8')
for seg in m3u8_obj.segments:
    print(seg.uri)
1
2
3
4
5
m3u8.load()中可以直接放入url

三、爬取视频

import re
import m3u8
import requests
from Crypto.Cipher import AES

# 保存的mp4文件名
name = "result.mp4"

# m3u8文件的url
url = "https://hls.videocc.net/f8f97d17d0/d/f8f97d17d0a21f1a1d84d214c5dcbfdd_1.m3u8?pid=1574769126087X1685817&device=desktop"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
}

# 获取m3u8文件内容
r = requests.get(url).content.decode()
# print(r)
m3u8_obj = m3u8.load(url)
ts_urls = []
for i, seg in enumerate(m3u8_obj.segments):
    if i<=10:
        # print(seg.uri)
        ts_urls.append(seg.uri)
print(ts_urls)

# 通过正则匹配下载key
k = re.findall(r'URI="(.*)"', r)[0]  # key的正则匹配
print(k)

# 此处加请求头访问key文件，否则相应可能为空
head = {
    'Origin': 'https://www.shiguangkey.com',
    'Referer': 'https://www.shiguangkey.com/video/2321?videoId=40168&classId=4179&playback=1',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
key = requests.get('https://hls.videocc.net/playsafe/f8f97d17d0/d/f8f97d17d0a21f1a1d84d214c5dcbfdd_1.key?token=4155fc5a-c118-4c1e-89ca-9838ddf4c5dd-w6175726', headers=head).content
# key = 0x798352326fcc8c33808758cb969f6ac9
print(key)
# 解密并保存ts
for ts_url in ts_urls:
	# 如果连接末尾没有.ts手动加上
    ts_name = ts_url.split("/")[-1] + '.ts'  # ts文件名
    print(ts_name)

    # 解密，new有三个参数，
    # 第一个是秘钥（key）的二进制数据，
    # 第二个使用下面这个就好
    # 第三个IV在m3u8文件里URI后面会给出，如果没有，可以尝试把秘钥（key）赋值给IV
    sprytor = AES.new(key, AES.MODE_GCM)
    print(sprytor)

    # 获取ts文件二进制数据
    print("正在下载：" + ts_name)
    ts = requests.get(ts_url).content
#
    # 密文长度不为16的倍数，则添加b"0"直到长度为16的倍数
    while len(ts) % 16 != 0:
        ts += b"0"

    print("正在解密：" + ts_name)

    # 写入mp4文件
    with open(name, "ab") as file:
        # # decrypt方法的参数需要为16的倍数，如果不是，需要在后面补二进制"0"
        file.write(sprytor.decrypt(ts))
        print("保存成功：" + ts_name)
print(name, "下载完成")



