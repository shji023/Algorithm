import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

time = 0
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while time < T:
    empty = [[0] * C for _ in range(R)]
    # 1
    for x in range(R):
        for y in range(C):
            if arr[x][y] != 0 and arr[x][y] != -1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                        cnt += 1
                        empty[nx][ny] += (arr[x][y] // 5)
                arr[x][y] = arr[x][y] - ((arr[x][y] // 5) * cnt)

    for i in range(R):
        for j in range(C):
            arr[i][j] += empty[i][j]
    # 2
    up = 0
    for r in range(R):
        if arr[r][0] == -1:
            up = r
            break
    empty = [[-2] * C for _ in range(R)]
    # 위쪽 순환
    for h in range(1, C):
        # 제일 윗줄
        empty[0][h - 1] = arr[0][h]
        # 공기청정기 위쪽 줄
        empty[up][h] = arr[up][h - 1]
        empty[up][1] = 0
        # 꺾이는 부분
    for v in range(1, up + 1):
        empty[v - 1][C - 1] = arr[v][C - 1]
        if arr[v][0] != -1:
            empty[v][0] = arr[v - 1][0]
    # 아래쪽 순환
    for h in range(1, C):
        empty[R - 1][h - 1] = arr[R - 1][h]
        empty[up + 1][h] = arr[up + 1][h - 1]
        empty[up + 1][1] = 0
    for v in range(up + 2, R):
        if arr[v - 1][0] != -1:
            empty[v - 1][0] = arr[v][0]
        empty[v][C - 1] = arr[v - 1][C - 1]
    for i in range(R):
        for j in range(C):
            if empty[i][j] != -2:
                arr[i][j] = empty[i][j]
    time += 1

print(sum(sum(arr,[]))+2)