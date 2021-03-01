import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(int(input()) for i in range(N))
a.sort()
start, end = 0, 0
answer = sys.maxsize

while start < N and end < N:
    sub = a[end]-a[start]
    if sub == M:
        answer = M
        break
    if sub < M:
        end += 1
        # end 만 증가하고 start 는 증가 못하도록
        continue
    start += 1
    answer = min(answer, sub)
print(answer)
