import heapq

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    min_h = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(min_h, i)

    while min_h:
        now = heapq.heappop(min_h)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(min_h, i)

    for i in result:
        print(i, end=' ')

topology_sort()