# N개의 최소공배수
def lcs(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arr):
    answer = 1
    for i in arr:
        answer = (answer * i)/lcs(answer, i)
    return answer

# JadenCase 문자열 만들기
# 공백이 여러개 있을 때는 그대로 출력해야함
def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer

# 행렬의 곱셈
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer

# 피보나치 수
def solution(n):
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append((answer[i-1] + answer[i-2])% 1234567)
    return answer[-1]

# 최솟값 만들기
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i, j in zip(A,B):
        answer += i*j
    return answer
'''
zip함수 설명
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
'''

# 최댓값과 최솟값
def solution(s):
    s = list(map(int, s.split()))
    a, b = min(s), max(s)
    return str(a) +" "+ str(b)

# 숫자의 표현
def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
    return answer

# 땅따먹기
def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][1], land[i-1][0], land[i-1][3])
        land[i][3] += max(land[i-1][1], land[i-1][2], land[i-1][0])
    answer = max(land[len(land)-1])
    return answer

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])


# 다음 큰 숫자

# 올바른 괄호
# 가장 큰 정사각형 찾기
# 124 나라의 숫자