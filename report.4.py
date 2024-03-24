Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
score = int(input("점수를 입력하세요 : "))
점수를 입력하세요 : 90
if score >= 90:
    print("장학생", end='')
elif score >= 60: # 90점 이상이 아니면서 60점 이상이라면
    print("합격", end='')
else:
    print("불합격", end='')

    
장학생
장학생
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    장학생
NameError: name '장학생' is not defined
print("입니다.^^")
입니다.^^

num = 5
if num % 2 == 0 :
    res = '짝수'
else :
    res = '홀수'

print(res)
홀수

hap=0

for n in range(3333,9999) :
    if n%1234 == 0 :

        continue
    if hap+n > 100000 :
        break
    hap = hap+n
    
SyntaxError: multiple statements found while compiling a single statement

hap=0

for n in range(3333,9999) :
    if n%1234 == 0:

        continue
    if hap+n > 100000 :
        break
    hap = hap+n

    
print(hap)
97063

hap=0

n = 1234
while n < 4568:
    if n % 444 == 0:
        hap+=n
    n+=1

    
print(hap)
23088
myData=[[n*m for n in range(1, 3)] for m in range(2,4)]
print(*myData, sep="\n")
[2, 4]
[3, 6]
>>> 
>>> nn = [ 100, 200, 300, 400, 500]
>>> nn[1] = 777
>>> nn[1] = [444, 555]
>>> nn[1:4] = [444, 555]
>>> nn[2:] = []
>>> nn=
SyntaxError: invalid syntax
>>> nn[1]
444
>>> nn[1:4]
[444]
>>> nn[2:]
[]
>>> nn[4]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    nn[4]
IndexError: list index out of range
>>> nn=[100,200,300,400,500]
>>> 
>>> nn[4]
500
>>> nn[-1]
500
>>> nn[-2]
400
>>> nn[1:4]
[200, 300, 400]
>>> nn[0:1]
[100]
>>> nn[2:-1]
[300, 400]
>>> nn[0::2]
[100, 300, 500]
>>> nn[::-1]
[500, 400, 300, 200, 100]
>>> nn[::-2]
[500, 300, 100]
