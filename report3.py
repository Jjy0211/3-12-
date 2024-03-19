Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("100")
100
>>> print(100)
100
>>> print(50+50)
100
>>> print("50+50")
50+50
>>> print ('%d / %d = %d' % (5,10,5/10))
5 / 10 = 0
>>> print("%04d"% 876)
0876
>>> print("%5s"%"CookBook")
CookBook
>>> print("%1.1f"%123.45)
123.5
>>> print("{2:d}{0:d}{1:d}".format(111,222,333))
333111222
>>> b=bin(1011)
>>> print(b)
0b1111110011
>>> int("1A",16)
26
>>> int('1002',2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int('1002',2)
ValueError: invalid literal for int() with base 2: '1002'
>>> int('1008',8)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int('1008',8)
ValueError: invalid literal for int() with base 8: '1008'
>>> int('AAFG',16)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int('AAFG',16)
ValueError: invalid literal for int() with base 16: 'AAFG'
int("1002",2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int("1002",2)
ValueError: invalid literal for int() with base 2: '1002'
print(int('1002',2))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(int('1002',2))
ValueError: invalid literal for int() with base 2: '1002'
sel=int(input("입력 진수 결정(16/10/8/2):"))
입력 진수 결정(16/10/8/2):16
num=input("값 입력:")
값 입력:10
num=input("값 입력:")
값 입력:12345678
if sel==16:
    num 10=int(num,16)
    
SyntaxError: invalid syntax
if sel==16:
    num 12345678=int(num,16)
    
SyntaxError: invalid syntax
num=12345678
hex_num=hex(num)
oct_num=oct(num)
bin_num=bin(num)

print("10진수 ==>", num)
10진수 ==> 12345678
print("16진수 ==> ", hex_num)
16진수 ==>  0xbc614e
print("8진수 ==>,oct_num)
      
SyntaxError: unterminated string literal (detected at line 1)
print("8진수 ==>"\,oct_num)
      
SyntaxError: unexpected character after line continuation character
print("8진수 ==>"",oct_num)
      
SyntaxError: unterminated string literal (detected at line 1)
print("8진수 ==>",oct_num)
      
8진수 ==> 0o57060516
print("2진수 ==> ", bin_num)
      
2진수 ==>  0b101111000110000101001110
