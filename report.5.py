Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ss = 'Python'
for i in range(0, len(ss)):
    print(ss[i] + '$',end='')

    
P$y$t$h$o$n$
s = '파이썬 ### CookBook $$$ @@@ 열공중 1234'
result = ''
for c in s:
    if c.isalpha():
        result += c

        
print(result)
파이썬CookBook열공중
inStr, outStr="Python",""
strLen = len(inStr)

for i in range(0, strLen):
    outStr+=inStr[strLen-(i+1)]

    
print("내용을 거꾸로 출력--> %s" % outStr)
내용을 거꾸로 출력--> nohtyP
def plus(v1,v2,v3):
    result = 0
    result = v1+v2+v3
    return result

hap = 0
hap = plus(100,200,300)
print(hap)
600
def f1():
    print(var)

    
>>> def f2():
...     var = 10
...     print(var)
... 
...     
>>> var = 100
>>> f1()
100
>>> f2()
10
>>> def addNumber(num):
...     if num == 1:
...         return 1
...     else:
...         return num + addNumber(num - 1)
... 
...     
>>> print(addNumber(100))
5050
>>> def myFunc(p1:int=1, p2:int=2, p3:int=3)
SyntaxError: expected ':'
>>> def myFunc(p1:int=1, p2:int=2, p3:int=3):
...     ret = p1 + p2 + p3
...     return ret
... 
>>> print("매개변수 없이 호출 ==>", myFunc())
매개변수 없이 호출 ==> 6
>>> print("매개변수가 1개로 호출 ==>, myFunc(1))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("매개변수가 1개로 호출 ==>", myFunc(1))
...       
매개변수가 1개로 호출 ==> 6
>>> print("매개변수가 2개로 호출 ==>", myFunc(1, 2))
...       
매개변수가 2개로 호출 ==> 6
>>> print("매개변수가 3개로 호출 ==>", myFunc(1, 2, 3))
...       
매개변수가 3개로 호출 ==> 6
