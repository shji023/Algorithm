N, M = map(int, input().split())
ch = []
for _ in range(N):
    a = list(map(int, input().split()))
    ch.append(min(a))
answer = max(ch)
print(answer)