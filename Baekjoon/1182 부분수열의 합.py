import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


def dfs(i, interval_sum):
    global cnt
    if i >= N:
        return
    interval_sum += arr[i]
    if interval_sum == S:
        cnt += 1
    dfs(i + 1, interval_sum - arr[i])
    dfs(i + 1, interval_sum)


dfs(0, 0)
print(cnt)
