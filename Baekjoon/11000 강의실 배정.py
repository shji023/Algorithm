import sys
import heapq
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr = sorted(arr, key=lambda x: x[0])
q = []
for i in arr:
    if q and q[0] <= i[0]:
        heapq.heappop(q)
    heapq.heappush(q, i[1])
print(len(q))
