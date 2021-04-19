import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N = int(input())
a = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    temp = [d]
    q = [d]
    for _ in range(g+1):
        for k in q:
            x += dx[k]
            y += dy[k]
            a[x][y] = 1
        q = [(i+1) % 4 for i in temp]
        q.reverse()
        temp = temp + q
result = 0
for i in range(100):
    for j in range(100):
        if a[i][j] and a[i][j + 1] and a[i + 1][j] and a[i + 1][j + 1]:
            result += 1
print(result)
