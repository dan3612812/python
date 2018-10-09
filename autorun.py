#! python3
import time  # 延遲
import pyautogui as auto  # 滑鼠鍵盤控制

auto.PAUSE = 0.25
auto.FAILSAFE = True  # 當滑鼠移到最左上角 強制退出python
width, height = auto.size()  # 取得螢幕解析度size
# 回commit
# 點開漂流 35 970
####------開啟儲放帳密檔案-------####

f = open('acc.txt', 'r')
all_f = f.read()
spf = all_f.split('\n')
###----------------------------####
###------開啟遊戲 滑鼠控制----###


def autoopen():
    auto.doubleClick(35, 970)  # 點擊遊戲  40 780
    # 允許 座標 1050 570
    # auto.moveTo(1050, 570, duration=0.25)
    auto.click(780, 670, button='left')  # 進入遊戲 780 670
    auto.click(950, 590, button='left')  # 確定950 590
    auto.click(820, 760, button='left')  # 開始更新820 760
    ca = True
    while(ca):
        ca = not(auto.pixelMatchesColor(745, 766, (255, 255, 255)))
        time.sleep(0.25)
    auto.click(820, 760, button='left')  # 開始執行檔案
    time.sleep(0.25)
    auto.click(870, 1035, button='left')  # 同意 870 1035
    auto.click(970, 690, button='left')  # 970 690
    time.sleep(2)
    auto.moveTo(320, 10)  # 移動滑鼠
###------------------------###


for i in range(0, 8, 1):
    sinacc = spf[i].split(':')  # 切開地i之資料 0序號 1acc 2pwd
    ihigh = i * 80
    iwidth = i * 30
    autoopen()
    # 拖曳 1433 10 第一個視窗高度 10 d=30  橫軸 d=-80
    auto.dragTo(1433 - ihigh, 10 + iwidth)
    ca = True
    while(ca):
        #im = auto.screenshot()
        #x, y, z = im.getpixel((1475 - ihigh, 285 + iwidth))
        #print(x + y + z)
        ca = not(auto.pixelMatchesColor(1650 - ihigh , 340 + iwidth, (255, 255, 255)))
        time.sleep(0.25)
    auto.doubleClick(1475 - ihigh, 285 + iwidth)  # 1430 280 選伺服器
    time.sleep(0.2)
    auto.click(1560 - ihigh, 260 + iwidth)  # 1560 263 選分流
    auto.doubleClick(1560 - ihigh, 260 + iwidth)  # 1530 280 選分流
    # time.sleep(0.2)

    #1500 250
    #time.sleep(8)
    ca =True
    while(ca):
        ca = not(auto.pixelMatchesColor(1500 - ihigh , 250 + iwidth, (255, 255, 255)))
        time.sleep(0.25)
    
    # auto.click(1530 - ihigh, 310 + iwidth)  # 點選密碼欄位
    # time.sleep(0.2)
    # auto.click(1530 - ihigh, 280 + iwidth)  # 點選帳號欄位
    # time.sleep(0.2)
    auto.typewrite(sinacc[1])  # 輸入帳號
    auto.press('enter')
    auto.typewrite(sinacc[2])  # 輸入密碼
    auto.press('enter')
    # 1450 470 角色一 登入
    # 1830 470 角色二 登入
    # 判斷要開哪知角色
    if(sinacc[3] == '1'):  # 字串跟int 不同
        poi = 1450
    else:
        poi = 1830

    time.sleep(0.8)
    auto.click(poi - ihigh, 470 + iwidth, button='left')
    auto.click(poi - ihigh, 470 + iwidth, button='left')
    time.sleep(0.6)
