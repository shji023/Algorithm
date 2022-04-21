import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    baduk = [[0]*N for _ in range(N)]
    baduk[N//2][N//2], baduk[(N//2)-1][(N//2)-1] = 2, 2
    baduk[N//2][(N//2)-1], baduk[(N//2)-1][N//2] = 1, 1
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for _ in range(M):
        y, x, color = map(int, input().split())
        x -= 1
        y -= 1
        if not baduk[x][y]:
            for i in range(8):
                nx = x + delta[i][0]
                ny = y + delta[i][1]
                reverse = []
                while True:
                    # 배열 밖
                    if nx < 0 or N-1 < nx or ny < 0 or N-1 < ny:
                        reverse = []
                        break
                    if baduk[nx][ny] == 0:
                        reverse =[]
                        break
                    if baduk[nx][ny] == color:
                        break
                    else:
                        reverse.append((nx, ny))
                    nx += delta[i][0]
                    ny += delta[i][1]
                if reverse:
                    baduk[x][y] = color
                for rx, ry in reverse:
                    baduk[rx][ry] = color
    b, w = 0, 0
    for i in range(N):
        for j in range(N):
            if baduk[i][j] == 1:
                b += 1
            elif baduk[i][j] == 2:
                w += 1
    print('#{} {} {}'.format(t, b, w))
