import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # 두 정점 사이의 간선이 여러 개라면 더 짧은 간선을 저장한다.
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print("0", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
