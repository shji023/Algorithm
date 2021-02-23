import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
arr.sort()
answer = 0
for i in range(N):
    if i == 0:
        start = arr[0][0]
        end = arr[0][1]
        answer = end-start
    else:
        if arr[i][0] <= end and arr[i][1] <= end:
            continue
        if arr[i][0] < end < arr[i][1]:
            answer += arr[i][1]-end
        if arr[i][0] > end:
            answer += arr[i][1] - arr[i][0]
        start = arr[i][0]
        end = arr[i][1]
print(answer)
