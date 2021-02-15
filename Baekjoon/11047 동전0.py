N, K = map(int, input().split())
a = list(int(input()) for _ in range(N))
a.sort(reverse=True)
cnt = 0
for coin in a:
    if coin <= K:
        cnt += K//coin
        K %= coin
print(cnt)