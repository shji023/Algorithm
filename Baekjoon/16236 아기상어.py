import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
second = 0
location = deque()
weight = 2
eat_cnt = 0

arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            location.append((i, j))
            arr[i][j] = 0
while True:
    # 한번의 상어 위치에 대한 이동
    visited = [[0] * N for _ in range(N)]
    eatable = []
    while location:
        a, b = location.popleft()
        # print(f"queue front: {a},{b}")
        # visited[a][b] += 1
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] > weight or visited[nx][ny] != 0:
                continue
            if 0 < arr[nx][ny] < weight:
                location.append([nx,ny])
                visited[nx][ny] = visited[a][b] + 1
                eatable.append([visited[nx][ny],nx,ny])
            if arr[nx][ny] == weight or arr[nx][ny] == 0:
            # else:
                visited[nx][ny] = visited[a][b] + 1
                location.append((nx, ny))
    if eatable:
        eatable = sorted(eatable)
        eat_cnt += 1
        if eat_cnt == weight:
            weight += 1
            eat_cnt = 0
        second += eatable[0][0]
        arr[eatable[0][1]][eatable[0][2]] = 0
        location.append((eatable[0][1], eatable[0][2]))
    else:
        break
print(second)