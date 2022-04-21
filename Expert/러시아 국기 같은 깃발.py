# DFS활용이 어려워 다중 for문 돌림
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, M= map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]
    Min = N*M
    whiteCnt = 0
    for white in range(0, N-2):
        for i in range(0, M):
            if arr[white][i] != "W":
                whiteCnt += 1
        blueCnt = 0
        for blue in range(white+1, N-1):
            for j in range(0, M):
                if arr[blue][j]!="B":
                    blueCnt += 1
            redCnt = 0
            for red in range(blue+1, N):
                for k in range(0, M):
                    if arr[red][k]!="R":
                        redCnt += 1
            cnt = whiteCnt+blueCnt+redCnt
            if Min > cnt:
                Min = cnt
    print(f'#{t+1} {Min}')





