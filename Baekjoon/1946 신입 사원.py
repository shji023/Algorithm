import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[0])
    min_arr = arr[0][1]
    for i in range(1, N):
        if arr[i][1] < min_arr:
            min_arr = arr[i][1]
            cnt += 1
    print(cnt)