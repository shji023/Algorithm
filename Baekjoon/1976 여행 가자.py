import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
parent = [0] * (N + 1)
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int,input().split()))

for i in range(1, N+1):
    parent[i] = i
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)
for i in range(M-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        print("NO")
        break
else:
    print("YES")
