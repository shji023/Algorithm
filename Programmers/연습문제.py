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
#히히히히
