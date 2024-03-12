Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> import random
>>> 
>>> def screenLeftclick(x,y) :
...     global r,g,b
...     turtle.pencolor((r,g,b))
...     turtle.pendown()
...     turtle.goto(x,y)
... 
...     
>>> def ScreenRightclick(x,y) :
...     turtle.penup()
...     turtle.goto(x,y)
... 
...     
>>> def screenMidclick(x,y) :
...     global r,g,b
...     tSize = random.randrange(1,10)
...     turtle.shapesize(tsize)
...     r=random.random()
...     g=random.random()
...     b=random.random()
... 
...     
>>> pSize=10
>>> r,g,b=0.0,0.0,0.0
>>> 
>>> turtle.title('거북이로 그림 그리기')
>>> turtle.shape('turtle')
>>> turtle.pensize(pSize)
>>> 
>>> turtlr.onscreenclick(screenLeftclick,1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    turtlr.onscreenclick(screenLeftclick,1)
NameError: name 'turtlr' is not defined. Did you mean: 'turtle'?
yes
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
turtle.onscreenclick(screenLeftclick,1)
turtle.onscreenclick(screenmidclick,2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    turtle.onscreenclick(screenmidclick,2)
NameError: name 'screenmidclick' is not defined. Did you mean: 'screenMidclick'?
turtle.onscreenclick(screenMidclick,2)
turtle.onscreenclick(screenrightclick,3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    turtle.onscreenclick(screenrightclick,3)
NameError: name 'screenrightclick' is not defined. Did you mean: 'ScreenRightclick'?
yes
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
turtle.onscreenclick(screenRightclick,3)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    turtle.onscreenclick(screenRightclick,3)
NameError: name 'screenRightclick' is not defined. Did you mean: 'ScreenRightclick'?

turtle.onscreenclick(screenLeftclick,1)
turtle.onscreenclick(screenMidclick,2)
turtle.onscreenclick(screenRightclick,3)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    turtle.onscreenclick(screenRightclick,3)
NameError: name 'screenRightclick' is not defined. Did you mean: 'ScreenRightclick'?
turtle.onscreenclick(ScreenRightclick,3)

turtle.done()
remove
