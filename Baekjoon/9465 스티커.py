import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    for j in range(1, n):
        if j == 1:
            s[0][j] += s[1][j-1]
            s[1][j] += s[0][j-1]
        else:
            s[0][j] += max(s[1][j-1], s[1][j-2])
            s[1][j] += max(s[0][j-1], s[0][j-2])
    print(max(s[0][n-1], s[1][n-1]))
