'''
이분 매칭(Bipartite Matching)
이분 그래프에서 A 그룹의 정점에서 B 그룹의 정점으로 간선을 연결할 때,
A 그래프의 하나의 정점이 B 그래프 하나의 정점만 가지도록 구성된 것
이분 그래프(Bipartite Graph)
정점을 두개의 그룹으로 나누었을 때,
존재하는 모든 간선의 양 끝 정점이 서로 다른 그룹에 속하는 형태의 그래프
'''

# PyPy3 제출
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[]*(N+1)]
for i in range(1, N+1):
    arr.append(list(map(int, input().split()))[1:])
cnt = 0
task = [0]*(M+1)

def dfs(n):
    if visited[n]:
        return 0
    visited[n] = 1
    for a in arr[n]:
        if task[a] == 0 or dfs(task[a]):
            task[a] = n
            return 1
    return 0

for i in range(N):
    visited = [0]*(N+1)
    if dfs(i+1):
        cnt += 1

print(cnt)