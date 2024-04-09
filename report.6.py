Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> window = Tk()
>>> 
>>> def rdo_change():
...      if var.get()==1:
...          label1.configure(text="벤츠")
...      else:
...          label1.configure(text="포르쉐")
... 
...          
>>> var=IntVar()
>>> rdo1=Radiobutton(window,text="벤츠",variable=var,value=1)
>>> rdo2=Radiobutton(window,text="포르쉐",variable=var,value=2)
>>> label1=Label(window, text="선택한 차량",fg="red")
>>> 
>>> rdo1.pack()
>>> rdo2.pack()
>>> label1.pack()
>>> 
>>> window.mainloop()
>>> 
>>> 
>>> from tkinter import *
>>> window = Tk()
>>> 
>>> button1 = Button(window, text = "버튼1")
>>> button2 = Button(window, text = "버튼2")
>>> button3 = Button(window, text = "버튼3")
>>> 
>>> button1.pack(side =LEFT)
>>> button2.pack(side =LEFT)
>>> button3.pack(side =LEFT)
>>> 
>>> window.mainloop()

... 
... 


