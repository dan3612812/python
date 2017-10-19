#! python3
import pyautogui as auto  # 鍵盤滑鼠控制
import time # 延遲
import datetime

auto.PAUSE = 0.1  # 每個函數暫停1.5秒
auto.FAILSAFE = True  # 當滑鼠移到最左上角 強制退出python
width, height = auto.size()  # 取得螢幕解析度size
# 1920,1080
''' 175.182.3.210
for i in range(10):
    auto.moveTo(300, 300, duration=0.25)  # 絕對座標 duration 移動的時間
    auto.moveTo(400, 300, duration=0.25)
    auto.moveTo(400, 400, duration=0.25)
    auto.moveTo(300, 400, duration=0.25)

for i in range(10):
    auto.moveRel(100, 0, duration=0.25)  # 相對座標
    auto.moveRel(0, 100, duration=0.25)
    auto.moveRel(-100, 0, duration=0.25)
    auto.moveRel(0, -100, duration=0.25)
'''
#取得 0.2秒 print一次目前鼠標位子
'''
z = 1
while(z > 0):
    x, y = auto.position()  # 獲取現在鼠標位子
    print(x, y)
    time.sleep(0.2)
'''
# auto.click(x-cur_x,y-cur_y,button='left')//x,y,滑鼠點擊左鍵  left middle right
# auto.click(button='left')
# auto.doubleClick(button='left')

# 拖曳 絕對座標
'''
for i in range(1,10):
    auto.dragTo(300-i*10,300-i*10,duration=0.0)
    auto.dragTo(300-i*10,400-i*10,duration=0.0)
    auto.dragTo(400-i*10,400-i*10,duration=0.0)
    auto.dragTo(400-i*10,300-i*10,duration=0.0)
'''
# 拖曳 相對座標
# auto.dragRel(100,0,duration=0.0)

# auto.scroll(200)  #pixel
'''

im = auto.screenshot()
# 取得某一點座標像素
x, y, z = im.getpixel((50, 200))
# 51 51 51
# 判斷螢幕座標點像素是否等於某像素
auto.pixelMatchesColor(50, 200, (51, 51, 51))  # ture False
''' 
# 用圖片搜尋螢幕
#print(auto.locateOnScreen('22.png'))
'''
x, y = auto.center(auto.locateOnScreen('22.png'))
auto.doubleClick(x,y)
'''
#鍵盤輸入
'''
auto.typewrite('python autogui.py',0.0)
auto.press('enter')
print(datetime.datetime.now())
'''
'''
for i in range(1,10):
    auto.hotkey('ctrlright','v')
'''