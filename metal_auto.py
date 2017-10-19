# python3

import time  # 延遲
import pyautogui as auto  # 滑鼠鍵盤控制


# 確認 1730 990
# start 963 214
# time.sleep(4)
time.sleep(2)

auto.moveTo(963,214,duration=0.5)
auto.click(963, 214, button='left')
time.sleep(0.5)
auto.mouseUp(button='left')


time.sleep(8)


auto.typewrite('x')
auto.moveTo(1700, 741)
auto.typewrite('w')
auto.typewrite('w')
auto.keyDown('d')
time.sleep(5)
auto.keyUp('d')
time.sleep(300)
# 1700 800
auto.click(1700, 800, button='left')
time.sleep(1)
auto.click(1700, 800, button='left')
