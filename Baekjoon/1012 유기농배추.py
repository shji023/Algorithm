# 가로세로가 헷갈렸다.
# 1인 부분을 dfs 탐색하고 탐색한 구간은 0 으로 바꿈
# 탐색이 끝나면 result +=1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return
    if graph[x][y] == 0:
        return
    graph[x][y] = 0
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)


for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    result = 0
    for q in range(N):
        for t in range(M):
            if graph[q][t] == 1:
                dfs(q, t)
                result += 1
    print(result)