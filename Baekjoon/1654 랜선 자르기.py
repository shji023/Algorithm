import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = list(int(input()) for _ in range(K))
start = 1
end = max(arr)

while start <= end:
    total = 0
    mid = (start+end)//2
    for x in arr:
        total += x//mid
    if total >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)