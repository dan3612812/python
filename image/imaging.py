#!python3
# https://yungyuc.github.io/oldtech/python/python_imaging.html

from PIL import Image
#import numpy as np
im = Image.open("captcha.png")
# show image information
# print(im.format, im.size, im.mode)  # 圖片資訊
# im.save('fileout.jpg')  # 轉換格式存檔

#--------圖片縮放---
# 轉換大小 11,3 使用的內插法是哪種 BILINEAR 品質較好 可不填 NEAREST取最近點
#nim = im.resize((11, 3), Image.BILINEAR)
# nim.save('resize.jpg')
# print(nim.format, nim.size, nim.mode)

#------單純圖片旋轉
# nim =im.rotate(90)
# nim.save('rotate.jpg')

#----圖片與尺寸選轉
# nim =im.transpose(Image.ROTATE_90)
# nim.save('transpose.jpg')

#----執行較快的thumbnail
#im.thumbnail( (400,100) )
#im.save( "thumbnail.jpg" )

#-- 修改圖形內容  paste()