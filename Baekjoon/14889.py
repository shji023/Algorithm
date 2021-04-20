# 조합 사용
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

numlist = [i for i in range(n)]
Min = float('inf')


def solve():
    global Min
    for c in combinations(numlist, n // 2):
        # 절반으로 나눔
        start = list(c)
        link = list(set(numlist) - set(c))

        # 능력치 계산은 두사람씩
        start_comb = list(combinations(start, 2))
        link_comb = list(combinations(link, 2))

        start_sum = 0
        for x, y in start_comb:
            start_sum += arr[x][y] + arr[y][x]

        link_sum = 0
        for x, y in link_comb:
            link_sum += arr[x][y] + arr[y][x]

        if Min > abs(start_sum - link_sum):
            Min = abs(start_sum - link_sum)


solve()
print(Min)