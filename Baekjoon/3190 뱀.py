import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
# 보드 초기화
arr = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    arr[i - 1][j - 1] = 1
L = int(input())
apple = deque()
for _ in range(L):
    x, c = input().split()
    apple.append([int(x), c])


def change(d, C):
    if d == 0:
        if C == 'L':
            return 3
        elif C == 'D':
            return 2
    elif d == 1:
        if C == 'L':
            return 2
        elif C == 'D':
            return 3
    elif d == 2:
        if C == 'L':
            return 0
        elif C == 'D':
            return 1
    elif d == 3:
        if C == 'L':
            return 1
        elif C == 'D':
            return 0


def check(x, y):
    if [x, y] in snake:
        return False
    return True


snake = deque()
snake.append([0, 0])
d = 0
time = 0
# 동 서 남 북
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while True:
    x, y = snake[-1][0], snake[-1][1]
    x += direction[d][0]
    y += direction[d][1]
    if 0 <= x < N and 0 <= y < N:
        if not check(x, y):
            break
        snake.append([x, y])
        if arr[x][y] == 1:
            arr[x][y] = 0
        else:
            snake.popleft()
    else:
        break
    time += 1
    if apple and time == apple[0][0]:
        d = change(d, apple[0][1])
        apple.popleft()
print(time+1)