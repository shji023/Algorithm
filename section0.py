# 값 교환
a, b = 10, 20
a, b = b, a

# 변수타입
# int
a = 12345
print(type(a))

a = 12.123456789123456789
# 8바이트 까지만 출력되고 뒤에 데이터는 손실됨
print(a)
# float
print(type(a))

# ""와 '' 구분 x
a = 'student'
# str
print(type(a))

# 출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
# 각 변수 사이를 sep로 지정해라
print(a, b, c, sep=',')
print(a, b, c, sep='\n')
# 1 2 3
print(a, end=' ')
print(b, end=' ')
print(c)

# 변수 입력과 연산자
# str
a = input("숫자를 입력하세요 : ")
print(a)
a, b = input("숫자를 입력하세요 : ").split()
# int
a = int(a)
b = int(b)
# map
a, b = map(int, input("숫자를 입력하세요 : ").split())
# 몫 연산자
print(a//b)
# 나머지 연산자
print(a%b)
# 거듭제곱
print(a**b)
a = 4.3
b = 5
c = a+b
# 실수와 정수가 연산되면 넓은 범위로 출력 float
print(type(c))

# 조건문 if(분기, 중첩)
x = 7
if x == 7:
    print("Lucky")

x = 15
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")

x = 10
if x > 0 and x < 10:
    print("10보다 작은 자연수")

x = 10
if a < x < 10:
    print("10보다 작은 자연수")

x = 10
if x > 0:
    print("양수")
else:
    print("음수")

# 반복문(for, while)
# [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9]
a = range(10)
# [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
a = range(1, 11)
print(list(a))

# 0 부터 9까지
for i in range(10):
    print("hello")

# i 내림차순으로 작아짐
for i in range(10, 0, -1):
    print("hello")

i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 10
while i >= 1:
    print(i)
    i = i - 1

# 무한 반복
i = 1
while True:
    print(i)
    i += 1

# continue
# 홀수만 출력
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# for else
# break를 하면 1부터 5까지만 출력
# 정상적으로 for문 종료하면 11출력
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:
    print(11)

'''
반복문을 이용한 문제 풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수 출력하기
'''
# 1)
N = int(input("N을 입력하세요 : "))
for i in range(1, N+1):
    if i % 2 == 0:
        continue
    else:
        print(i)

# 2)
N = input("N을 입력하세요 : ")
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)

# 3)
N = int(input("N을 입력하세요 : "))
for i in range(1, N+1):
    if N % i == 0:
        print(i)

#중첩 반복문(2중 for문)
for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

# 문자열과 내장함수
# 모든 문자 대문자화, 소문자화
msg = "It is Time"
print(msg.upper())
print(msg.lower())

tmp = msg.upper()
# T의 인덱스 찾아서 출력
print(tmp.find('T'))
# T의 개수 출력
print(tmp.count('T'))
# 처음부터 index 2 전까지 출력
print(msg[:2])
# 인덱스 3번부터 인덱스 5번 전까지 출력
print(msg[3:5])
# msg의 길이 출력. 공백포함
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

# 대문자만 출력
for x in msg:
    if x.isupper():
        print(x, end=' ')
# 소문자만 출력
for x in msg:
    if x.islower():
        print(x, end=' ')
# 알파벳만 출력
for x in msg:
    if x.isalpha():
        print(x, end=' ')
# 대문자 아스키 넘버 출력 A = 65, Z = 90
tmp = 'AZ'
for x in tmp:
    print(ord(x))
# 소문자 아스키 넘버 출력 A = 97, Z = 122
tmp = 'az'
for x in tmp:
    print(ord(x))
# 아스키 넘버에 해당하는 문자 출력
tmp = 65
print(chr(tmp))

#리스트와 내장함수(1)

import random as r
a = []
print(a)
b = list()
print(b)

a = [1, 2, 3, 4, 5]
# 0 부터 10까지
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(range(1, 11))

# [1, 2, 3, 4, 5, 6]
a.append(6)
# [1, 2, 3, 7, 4, 5, 6]
a.insert(3, 7)
# [1, 2, 3, 7, 4, 5]
a.pop()
# [1, 2, 3, 4, 5]
a.pop(3)
# [1, 2, 3, 5]
a.remove(4)
# 3
print(a. index(5))

a = list(range(1, 11))
print(sum(a))
print(max(a))
print(min(a))
# 무작위로 섞음
r.shuffle(a)
# 오름차순 정렬
a.sort()
# 내림차순 정렬
a.sort(reverse=True)
# 빈 리스트
a. clear()

# 리스트와 내장함수
a = [23, 12, 36, 53, 19]
# [23, 12, 36]
print(a[:3])
# [12, 36, 53]
print(a[1:4])
# 5
print(len(a))
# 23 12 36 53 19
for i in range(len(a)):
    print(a[i], end=' ')
for x in a:
    print(x, end=' ')
# (0,23)(1,12)(2,36)(3,53)(4,19)
for x in enumerate(a):
    print(x)
# 튜플
# 튜플값은 절대 변경 불가능
# 리스트의 값은 변경 가능
b = (1, 2, 3, 4, 5)

# 0 23  1 12  2 36  3 53  4 19
for x in enumerate(a):
    print(x[0], x[1])
for index, value in enumerate(a):
    print(index, value)

# all 다 참이어야 참
if all(60 > x for x in a):
    print("Yes")
else:
    print("No")
# any 한번이라도 참이면 참
if any(15 > x for x in a):
    print("Yes")
else:
    print("No")

# 2차원 리스트 생성과 접근
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [0] * 10
# [[0,0,0],[0,0,0],[0,0,0]]
a = [[0]*3 for _ in range(3)]

# 함수 만들기
def add(a, b):
    c = a+b
    print(c)

add(3, 2)

# 소수
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end=' ')

# 람다 함수
# 익명의 함수
# 2
def plus_one(x):
    return x+1
print(plus_one(1))

# 3
plus_two = lambda x:x+2
print(plus_two(1))

# [2, 3, 4]
def plus_one(x):
    return x+1
a = [1, 2, 3]
print(list(map(plus_one, a)))

print(list(map(lambda x: x+1, a)))

# sort 할 때 lambda 잘 씀