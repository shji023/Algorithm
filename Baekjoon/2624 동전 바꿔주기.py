import sys

input = sys.stdin.readline

T = int(input())
k = int(input())
arr = [[0, 0]]
for i in range(k):
    arr.append(list(map(int, input().split())))

arr.sort()
dp = [[0] * (T + 1) for _ in range(k + 1)]

for i in range(k + 1):
    dp[i][0] = 1

for i in range(1, k + 1):
    for num in range(arr[i][1] + 1):
        for j in range(T + 1):
            temp = j + num * arr[i][0]
            if temp == 0:
                continue
            if temp < T + 1:
                dp[i][temp] += dp[i - 1][j]
            else:
                break

print(dp[k][T])
