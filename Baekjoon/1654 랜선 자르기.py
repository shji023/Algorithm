import sys
input = sys.stdin.readline
K, N = map(int, input().split())
arr = list(int(input()) for _ in range(K))

start = 0
end = 10000000000

while start <= end:
    total = 0
    mid = (start+end)//2
    for x in arr:
        total += x//mid
    if total >= N:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(end)
