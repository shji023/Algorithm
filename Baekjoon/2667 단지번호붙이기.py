import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
arr = []


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            arr.append(cnt)
            cnt = 0
            result += 1

arr.sort()
print(result)
for i in range(len(arr)):
    print(arr[i])
