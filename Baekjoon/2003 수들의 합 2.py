N, M = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
interval_sum = 0
end = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += a[end]
        end += 1
    if interval_sum == M:
        cnt += 1
    interval_sum -= a[start]

print(cnt)
