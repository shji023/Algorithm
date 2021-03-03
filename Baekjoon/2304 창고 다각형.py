import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
start = arr[0][0]
end = arr[N-1][0]
temp = [[0, 0]for _ in range(end-start+1)]
for x in range(len(temp)):
    for y in range(N):
        if arr[y][0]-start == x:
            temp[x][0] = arr[y][0]
            temp[x][1] = arr[y][1]

left_max = 0
right_max = 0
result = 0
for i in range(len(temp)):
    for j in range(i+1):
        if temp[j][1] > left_max:
            left_max = temp[j][1]
    for j in range(i, len(temp)):
        if temp[j][1] > right_max:
            right_max = temp[j][1]
    result += min(left_max, right_max)
    left_max = 0
    right_max = 0
print(result)