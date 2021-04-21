import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i, j])
        elif arr[i][j] == 1:
            house.append([i, j])
chicken = (combinations(chicken, m))
result = 100000000
for k in chicken:
    dist = 0
    for i, j in house:
        min_num = 100000000
        for x, y in k:
            min_num = min(min_num, abs(x-i)+abs(y-j))
        dist += min_num
    result = min(result, dist)
print(result)