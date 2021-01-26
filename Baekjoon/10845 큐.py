import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        queue.append(int(a[1]))
    elif a[0] == 'pop':
        if not queue:
            print('-1')
        else:
            print(queue[0])
            queue.popleft()
    elif a[0] == 'front':
        if not queue:
            print('-1')
        else:
            print(queue[0])
    elif a[0] == 'back':
        if not queue:
            print('-1')
        else:
            print(queue[-1])
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)