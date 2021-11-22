import sys
sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def solution(x, y, n):
    global white, blue
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n // 2)
                solution(x+n//2, y, n // 2)
                solution(x+n//2, y+n//2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0, 0, N)
print(white)
print(blue)