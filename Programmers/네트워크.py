from collections import deque


def bfs(computers, i, visited,n):
    visited[i] = True
    queue = deque([i])
    while queue:
        v = queue.popleft()
        visited[v] = True
        for t in range(n):
            if computers[v][t] == 1:
                if visited[t] == False:
                    queue.append(t)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            bfs(computers, i, visited, n)
            answer += 1
    return answer

# DFS
# 그래프의 연결된 정보를 새 그래프 graph에 입력한다
# graph돌면서 이미 visited 가 0이 아닌 경우(다른 네트워크에 연결되어있지 않은 경우)에만 새로 탐색
def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(graph, i, visited)
    return True


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0] * (n)
    for i in range(n):
        for j in range(n):
            if (computers[i][j] == 1) and (i != j):
                graph[i].append(j)
    for i in range(n):
        if visited[i] != 1:
            if dfs(graph, i, visited):
                answer += 1
    return answer