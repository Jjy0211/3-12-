Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from time import *
>>> fnameList = ["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif","jeju5.gif","jeju6.gif","jeju7.gif","jeju8.gif","jeju9.gif"]
>>> num = 0
>>> def clickNext():
...     global num
...     if num == len(fnameList) - 1:
...         num = 0
...     else:
...         num += 1
...     pLabel.configure(text=fnameList[num])
... 
...     
>>> def clickPrev():
...     global num
...     if num == 0:
...         num = len(fnameList) - 1
...     else:
...         num -= 1
...     pLabel.configure(text=fnameList[num])
... 
...     
>>> window = Tk()
>>> window.geometry("700x100")
''
>>> btnPrev = Button(window,text="<< 이전",command=clickPrev)
>>> btnNext = Button(window,text="다음 >>",command=clickNext)
>>> pLabel = Label(window,text="파일명",font=("궁서체",20),fg="blue")
>>> btnPrev.place(x=150,y=10)
>>> btnNext.place(x=500,y=10)
>>> pLabel.place(x=300,y=10)
>>> window.mainloop()
