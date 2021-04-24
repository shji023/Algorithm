import sys

input = sys.stdin.readline


def dfs(x, s):
    if x == m:
        for i in res:
            print(i, end=' ')
        print()
    else:
        for i in range(s, n+1):
            res[x] = i
            dfs(x+1, i+1)


n, m = map(int, input().split())
res = [0] * m
dfs(0, 1)