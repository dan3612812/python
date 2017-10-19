#! python2
# coding=UTF-8
#from Tkinter import *
import Tkinter as tk

win = tk.Tk()
win.title("first tk test ")
# win.resizable(0, 0)  # 禁止使用者調整大小
f = open('text.txt', 'a+')
x = 0


def clickOK():
    global x
    x += 1
    label.configure(text="Click OK " + str(x) + " times")


button = tk.Button(win, text="OK", command=clickOK)
button.pack()
# if from Tkinter import * then label=Label(win,text="Hello World!")
label = tk.Label(win, text="Hello World!")  # 容器物件變數,[元件選項]
label.pack()  # 顯示元件 將元件 由上而下水平置中順序排版
#button = tk.Button(win, text="OK")
# button.pack()
#rb = tk.Radiobutton(win, text="cc")
# rb.pack()
en1 = tk.Entry(win)
en1.pack()
en2 = tk.Entry(win)
en2.pack()
en1.insert(1, "asdfasdf")
x = len(en1.get())
en1.delete(0, x)
print(x)


def show():
    print("First name: %s aaa: %s", en1.get(), en2.get())


def writefile():
    f.write("acc: %s ,pwd: %s ", en1.get(), en2.get())


bu = tk.Button(win, text="OK", command=writefile)
bu.pack()

#pw = tk.PanedWindow(win)
#rb2 = tk.Radiobutton(pw, text="aa")
# pw.pack()


'''
label = tk.Label(win, text="用grid")
label.grid(column=0, row=0)
button = tk.Button(win, text="OK")
button.grid(column=0, row=1)
'''


win.mainloop()  # 最後顯現
