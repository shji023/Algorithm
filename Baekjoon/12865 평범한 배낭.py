import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
bag = [[0]*(K+1) for _ in range(N+1)]
arr.insert(0, [0, 0])

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < arr[i][0]:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(arr[i][1] + bag[i-1][j-arr[i][0]], bag[i-1][j])
print(bag[N][K])