import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0


# 바이러스를 퍼뜨리는 bfs함수
def bfs():
    global answer
    temp = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append([nx, ny])
    cnt = 0
    for i in temp:
        cnt += i.count(0)
    answer = max(answer, cnt)


# 벽을 세울 수 있는 공간에 벽 3개를 세우는 모든 경우의수
def wall(x):
    if x == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(x + 1)
                    arr[i][j] = 0


queue = deque()
wall(0)
print(answer)
