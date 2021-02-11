N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = 0
start = 0
end = N - 1
while start <= end:
    mid = (start + end) // 2
    if a[mid] == M:
        answer = mid
        break
    elif a[mid] > M:
        end = mid - 1
    else:
        start = mid + 1
print(answer + 1)