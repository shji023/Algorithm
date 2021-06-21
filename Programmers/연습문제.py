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

# 자연수 뒤집어 배열로 만들기
def solution(n):
    numList = list(str(n))
    temp = []
    for i in range(len(numList)-1,-1,-1):
        temp.append(numList[i])
    answer = [int(i) for i in temp]
    return answer

# 자릿수 더하기
def solution (n):
    numList = list(map(int, str(n)))
    sumList = 0
    for i in numList:
        sumList += i
    return sumList

# 이상한 문자 만둘기
def solution(s):
    sample = list(s)
    index = 0
    for i in range(len(s)):
        if sample[i].isalpha():
            if index % 2 == 0:
                sample[i] = sample[i].upper()
            else:
                sample[i] = sample[i].lower()
            index += 1
        elif sample[i] == " ":
            index = 0
    return ("".join(str(j) for j in sample))

#약수의 합
def solution(n):
    mid = int(pow(n, 0.5))
    arr = []
    for i in range(1, mid + 1):
        if n % i == 0:
            arr.append(i)
    length = len(arr)
    for j in range(length):
        if n/arr[j] != arr[j]:
            arr.append(n/arr[j])
    return(int(sum(arr)))

# 시저암호
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A') + n)%26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)

# 문자열을 정수로 바꾸기
def solution(s):
    arr = list(s)
    if arr[0] == "+":
        arr.pop(0)
        return int("".join(arr))
    elif arr[0] == "-":
        arr.pop(0)
        return -1 * int("".join(arr))
    else:
        return int(s)

# 수박?
def solution(n):
    answer = []
    for i in range(n):
        if i % 2 == 0:
            answer.append("수")
        else:
            answer.append("박")
    return "".join(answer)

# 소수 찾기
def solution(n):
    ch = [0]*(n+1)
    cnt = 0
    for i in range(2, n+1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i, n+1, i):
                ch[j] = 1
    return cnt

# 서울에서 김서방 찾기
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            return "김서방은 "+str(i)+"에 있다"

# 문자열 다루기 기본
def solution(s):
    if s.isdigit():
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    else:
        return False

# 문자열 내림차순으로 배치하기
def solution(s):
    arr = list(s)
    arr.sort(reverse=True)
    return "".join(arr)

# 문자열 내 p와 y의 개수
def solution(s):
    new = s.lower()
    print(new)
    cntP, cntY = 0, 0
    for i in range(len(s)):
        if new[i] == "p":
            cntP += 1
        elif new[i] == "y":
            cntY += 1
    if cntP > 0 or cntY > 0:
        if cntP == cntY:
            return True
        else:
            return False
    else:
        return True

# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

# 두 정수 사이의 합
def solution(a, b):
    Sum = 0
    if a>b:
        for i in range(b, a+1):
            Sum += i
    elif a<b:
        for i in range(a, b+1):
            Sum += i
    else:
        return a
    return Sum

# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
    if not answer:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer

# 같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
