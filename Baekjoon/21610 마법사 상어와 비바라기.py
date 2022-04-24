# pypy3 제출
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ix = [-1, -1, 1, 1]
iy = [-1, 1, -1, 1]
cloud = deque([(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)])

# 명령어의 갯수만큼
for i in range(M):
    # 한 명령어의 횟수만큼
    for j in range(move[i][1]):
        # 구름 칸 모두 다
        visited = [[False] * N for _ in range(N)]
        for k in range(len(cloud)):
            nx = dx[move[i][0]-1] + cloud[k][0]
            ny = dy[move[i][0]-1] + cloud[k][1]
            if nx < 0:
                nx = N - ((nx*-1) % N)
            elif nx >= N:
                nx = (nx % N)
            if ny < 0:
                ny = N - ((ny * -1) % N)
            elif ny >= N:
                ny = (ny % N)
            cloud[k] = (nx, ny)
            visited[nx][ny] = True
    for p in range(len(cloud)):
        arr[cloud[p][0]][cloud[p][1]] += 1
    for q in range(len(cloud)):
        cnt = 0
        for t in range(4):
            qx = ix[t] + cloud[q][0]
            qy = iy[t] + cloud[q][1]
            if qx < 0 or qx >= N or qy < 0 or qy >= N:
                continue
            if arr[qx][qy] > 0:
                cnt += 1
        arr[cloud[q][0]][cloud[q][1]] += cnt

    temp_cloud = deque([])
    idx = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] >= 2 and not visited[x][y]:
                temp_cloud.append((x, y))
                arr[x][y] -= 2
    cloud = temp_cloud
result = 0
print(sum(sum(b) for b in arr))