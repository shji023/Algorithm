import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽방향으로 회전 북->서, 서->남, 남->동, 동->북
def changeLeft(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def find(x, y, d):
    cnt = 1
    arr[x][y] = 2
    while True:
        # 네방향 회전
        for _ in range(4):
            empty = 0
            d = changeLeft(d)
            nx = x + dx[d]
            ny = y + dy[d]
            # 유효범위 안, 빈칸
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                cnt += 1
                x = nx
                y = ny
                arr[nx][ny] = 2
                empty = 1
                break
        if empty == 0:
            # 후진
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
            if arr[x][y] == 1:
                break
    return cnt


result = find(r, c, d)
print(result)