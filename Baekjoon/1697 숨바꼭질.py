import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
Max = 100001

def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == K:
            print(time[v])
            return
        for i in (v-1, v+1, 2*v):
            if (0 <= i < Max) and time[i] == 0:
                time[i] = time[v] + 1
                queue.append(i)

time = [0]*Max
bfs(N)