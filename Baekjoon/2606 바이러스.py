# DFS
# graph 해당 인덱스에 append
# 1번 시작으로 연결된 부분 visited 1로 바꾸기
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N+1)

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True
dfs(graph,1,visited)
print(sum(visited)-1)