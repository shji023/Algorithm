import sys

input = sys.stdin.readline

N = int(input())
T = []
P = []
dp = []
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
    dp.append(b)
dp.append(0)
for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
print(dp[0])

# 다른 접근

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [(0,0)]*N
for i in range(N):
    if i + arr[i][0] > N:
        continue
    accumulate_pay = 0
    for j in range(i):
        if dp[j][0] <= i and accumulate_pay<dp[j][1]:
            accumulate_pay = dp[j][1]
    dp[i] = (arr[i][0]+i,accumulate_pay+arr[i][1])
result = max(dp, key=lambda x : x[1])
print(result[1])