import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
while True:
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                queue = deque([])
                temp = deque([])
                queue.append((x, y))
                temp.append((x, y))
                visited[x][y] = True
                Sum = arr[x][y]
                while queue:
                    a, b = queue.popleft()
                    for i in range(4):
                        nx = dx[i] + a
                        ny = dy[i] + b
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        if L <= abs(arr[a][b] - arr[nx][ny]) <= R and not visited[nx][ny]:
                            visited[nx][ny] = True
                            Sum += arr[nx][ny]
                            queue.append((nx, ny))
                            temp.append((nx, ny))
                if len(temp) > 1:
                    cnt += 1
                    for t in range(len(temp)):
                        arr[temp[t][0]][temp[t][1]] = Sum // len(temp)
    if cnt == 0:
        break
    answer += 1
print(answer)