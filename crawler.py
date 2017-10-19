#! python3
'''
import requests
res =requests.get('http://pala.tw/js-example/') #取得html 沒有js
print(res.text)
'''
# 讀的到js程式所渲染出來的html
'''
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-windows/bin/phantomJS')
driver.get('http://pala.tw/js-example/')
pageSource =driver.page_source
print(pageSource)
driver.close()
'''
# 撈取 html id class 特定資料 用python 3.5自帶 網頁解析器 解析效果沒 lxml好
'''
import requests
from bs4 import BeautifulSoup
tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
req = requests.get('http://pala.tw/class-id-example/')
soup = BeautifulSoup(req.content, 'html.parser')
print(soup)
'''
# 撈取 html id class 但用lxml
import requests
from bs4 import BeautifulSoup
tag = input("請輸入定位元素，class前面加上.，id前面加上# ")
req = requests.get('http://pala.tw/class-id-example/')
#req =requests.get('https://www.pixiv.net/search.php?s_mode=s_tag&word=%E9%B9%BF%E5%B3%B6')
soup = BeautifulSoup(req.text, 'lxml')

# 選出tag符合條件的 字串
# Calss ="_icon sprites-bookmark-badge" #pixiv 的熱門程度
tag = '.半糖'
for drink in soup.select('{}'.format(tag)):
    print(drink.get_text())
