import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))
left_max = 0
right_max = 0
result = 0
for i in range(W):
    for j in range(i+1):
        if arr[j] > left_max:
            left_max = arr[j]
    for j in range(i, W):
        if arr[j] > right_max:
            right_max = arr[j]
    result += min(left_max, right_max) - arr[i]
    left_max = 0
    right_max = 0
print(result)

