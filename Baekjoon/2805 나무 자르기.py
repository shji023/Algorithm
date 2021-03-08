# PyPy3 제출
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1, max(arr)

while start <= end:
    temp = 0
    mid = (start + end) // 2
    for i in arr:
        if i >= mid:
            temp += (i - mid)
    if temp >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)