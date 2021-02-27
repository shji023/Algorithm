import sys
input = sys.stdin.readline


def dfs(x, cnt):
    if cnt == 6:
        for i in range(k):
            if arr[i]:
                print(lotto[i], end=' ')
        print()
        return
    for i in range(x, k):
        arr[i] = True
        dfs(i + 1, cnt + 1)
        arr[i] = False


while True:
    lotto = list(map(int, input().split()))
    k = lotto[0]
    if k == 0:
        break
    arr = [False] * k
    lotto = lotto[1:]
    dfs(0, 0)
    print()
