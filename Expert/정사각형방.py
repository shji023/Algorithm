# for x, for y 돌면서 stack에 start로 넣음
# 상하좌우 돌면서 조건을 만족하면 stack에 돌고 계속 cnt += 1
# stack이 끝날때까지
# cnt가 Max면 교체
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def search(start):
    cnt = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        cnt += 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if arr[nx][ny] == arr[x][y] + 1:
                stack.append((nx, ny))
    return cnt
T = int(input())
for i in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    start = 0
    for x in range(N):
        for y in range(N):
            cnt = search((x, y))
            if Max < cnt:
                Max = cnt
                start = arr[x][y]
            elif cnt == Max:
                if arr[x][y] < start:
                    start = arr[x][y]
    print(f'#{i+1} {start} {Max}')
