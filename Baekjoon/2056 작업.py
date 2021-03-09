import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    indegree[i] = arr[0]
    for j in range(2, len(arr)):
        graph[i].append(arr[j])
for i in range(1, N+1):
    if graph[i]:
        temp = 0
        for j in graph[i]:
            temp = max(temp, indegree[j])
        indegree[i] += temp

print(max(indegree))