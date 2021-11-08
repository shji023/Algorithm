import sys
import heapq
sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
    heapq.heappush(h, int(input()))

if len(h) == 1:
    print(0)
else:
    answer = 0
    while len(h) > 1:
        Min = heapq.heappop(h)
        Min2 = heapq.heappop(h)
        answer += Min + Min2
        heapq.heappush(h, Min+Min2)
    print(answer)