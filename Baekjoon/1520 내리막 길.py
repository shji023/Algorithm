'''
DFS + DP로 풀어야하는 문제
접한 지점의 높이가 낮다고 해서 이미 탐색한 길이라면 해당 지점으로 부터 갈 수 있는 경로의 수만 받아옴
이렇게 DP와 DFS를 동시에 사용하기 위해서는 이미 탐색했던 길인지, 처음 가는 길인지 판단할 수 있어야 한다.
이 과정은 DP 배열의 초기값을 -1로 설정함으로 구분할 수 있다.
만약 탐색하려는 지점의 DP값이 초기값이라면 0으로 바꿔준 후, 그 지점부터 DFS를 다시 시작한다.
초기값이 아니라면 탐색을 한 지점이며 몇 갈래의 길이 파생되는지 정보를 이미 담고 있으므로 바로 그 값을 반환한다.

dp 배열 초기값 -1의 이유
(N - 1, M - 1)까지 갈 수 있는 경로가 없을 경우에는 DP[][] 값에 0 이 저장됨.
즉, '0'의 의미는 해당 좌표에서 도착점까지 갈 수 있는 경로가 0개인것 를 의미하고,
' -1' 의 의미는 아직 탐색을 진행하지 않은 좌표임을 의미한다.
'''

import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))