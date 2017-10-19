#! python3
# 先標題取代完 再簡轉繁
import os
from opencc import OpenCC

# 取代


def spec(ss):

    for i in range(linefcou):
        if(linef[i]=="END"):
            break
        spf = linef[i].split(':')
        #print(spf[0],spf[1])
        ss = ss.replace(spf[0], spf[1])
    return ss

# 修改檔案名稱

def modify(root):
    # 每個檔案
    for txt in os.listdir('.'):
        ss = str(txt)
        ss=spec(ss)
        ss = openCC.convert(ss)
        os.rename(txt, ss)
        print(ss)

# 讀檔
f = open('specific.txt', encoding='utf8')
all_f = f.read()
linef = all_f.split('\n')
linefcou = len(linef)


os.chdir('book')  # 切換工作目錄
openCC = OpenCC()
openCC.set_conversion('s2t')  # 翻譯或轉譯 語言選擇
for root in os.listdir('.'):
    if(os.path.isdir(root)):
        os.chdir(root)  # 切進符合條件目錄
        modify(root)
        os.chdir('../')  # 切回原本工作目錄
os.system("pause")