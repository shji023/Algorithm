N, M, K = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
cnt = 0
a.sort()
for i in range(M):
    if cnt != K:
        sum += max(a)
        cnt += 1
    else:
        sum += a[len(a)-2]
        cnt = 0
print(sum)

# 효율성을 고려한 답안 코드
# 가장 큰 수가 더해지는 횟수 계산하여 해결
N, M, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
result = 0
first = a[N-1]
second = a[N-2]


result += ((M//(K+1)) * K) * first
result += (M % (K+1)) * first
result += (M//(K+1)) * second

print(result)
