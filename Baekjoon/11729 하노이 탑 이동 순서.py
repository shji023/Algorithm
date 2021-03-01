import sys
input = sys.stdin.readline

n = int(input())
print(2**n -1)

def hanoi(n, s, other, e):
    if n == 0:
        return
    else:
        # 맨 밑 원판을 제외하고 나머지를 목적지가 아닌곳에
        hanoi(n-1, s, e, other)
        # 맨 밑 원판을 목적지에
        print(s, e, end=" ")
        print()
        # 목적지가 아닌곳에 옮겼던 그 원반들을 다시 맨밑 원판 위에
        hanoi(n-1, other, s, e)

hanoi(n, 1, 2, 3)