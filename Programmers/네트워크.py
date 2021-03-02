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