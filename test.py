f = open('text.txt', 'a+')
# f.seek(1,0)#  位移bit數,從文件開頭開始
# f.seek(1,1)# 位移bit數,從目前游標位置開始
# f.seek(1,2)# 位移bit數,從目前文件結尾開始
f.write("測試\n")
f.write("第二次寫入\n")
f.write("第三次寫入")
x = 4
y = 4
w = 9999
v = 9999
a = 12345678
b = 12345678
print (hex(id(x)))
print (hex(id(y)))
print (hex(id(w)))
print (hex(id(v)))
print (hex(id(a)))
print (hex(id(b)))