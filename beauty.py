#! python3
import requests as req
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os


def checkstr(s):
    s = s.replace(" ", "")
    le = s.find('[公告]')
    if (le == -1):
        le = s.find('[情報]')

    return le


def down_img(articles):
    for art in articles:
        #print(art.text, art['href'])
        req2 = req.get('https://www.ptt.cc' + art['href'])
        temp = art.text.replace(':', '') #名子
        temp =temp.replace(" ","") #空白
        temp = temp.replace('/','_')#時間
        #測試測是
        if(checkstr(temp)==-1):
            if not(os.path.isdir(os.path.join('download', temp))):  # 在download資料夾找尋 art.text
                os.makedirs(os.path.join('download', temp))
            img = all_image.findall(req2.text)
        # print(img)
        for i in set(img):  # 刪除重複
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))', i).group(1)
            print(ID)
            urlretrieve(i, os.path.join('download', temp, ID))


# soup = BeautifulSoup(res.text,'html.parser')
#-------- 爬每頁----#
if not(os.path.isdir('download')):
    os.makedirs('download')  # 建立資料夾
url = 'https://www.ptt.cc/bbs/beauty/index.html'
all_image = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')
for i in range(3):
    res = req.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    articles = soup.select('div.title a')
    paging = soup.select('div.btn-group-paging a')
    url2 = 'https://www.ptt.cc' + paging[1]['href']
    url = url2
    down_img(articles)
