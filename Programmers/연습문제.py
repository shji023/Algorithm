# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

# 행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    for i in range(n):
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer

# 핸드폰 번호 가리기
def solution(phone_number):
    temp = []
    n = len(phone_number)
    for i in range(n):
        if i < n-4:
            temp.append("*")
        else:
            temp.append(phone_number[i])
    answer = "".join(temp)
    return answer

# 하샤드 수
def solution(x):
    answer = True
    temp = str(x)
    num = 0
    for i in temp:
        num += int(i)
    if x % num != 0:
        answer = False
    return answer

# 평균 구하기
def solution(arr):
    Sum = 0
    for i in arr:
        Sum += i
    answer = Sum/len(arr)
    return answer

# 콜라츠 추측
def solution(num):
    answer = 0
    while num != 1:
        if answer <= 500:
            if num % 2 == 0:
                num = num/2
            elif num % 2 == 1:
                num = (num * 3) + 1
            answer += 1
        else:
            answer = -1
            break
    return answer

# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    a = n
    b = m
    while b > 0:
        a, b = b, a % b
    answer.append(a)
    answer.append(n*m/a)
    return answer

# 짝수와 홀수
def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 제일 작은 수 제거하기
def solution(arr):
    if len(arr) > 1:
        arr.remove((min(arr)))
        return arr
    else:
        return [-1]

# 정수 제곱근 판별
import math

def solution(n):
    num = math.sqrt(n)
    if num == int(num):
        return pow(num+1, 2)
    else:
        return -1

# 정수 내림차순으로 배치하기
def solution(n):
    numList = list(str(n))
    numList.sort(reverse=True)
    answer = "".join(numList)
    return int(answer)