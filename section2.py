# k번째 약수 *
a = []
n, k = map(int, input().split())
for i in range(1, n + 1):
    if n % i == 0:
        a.append(i)
if len(a) < k:
    print(-1)
else:
    print(a[k - 1])

# k 번째 수
T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(i+1, a[k-1]))

# k번째 큰 수
N, K = map(int, input().split())
a = list(map(int, input().split()))
# 중복제거 자료구조 set()
res = set()
for x in range(N):
    for y in range(x+1,N):
        for z in range(y+1,N):
            res.add(a[x]+a[y]+a[z])
temp = list(res)
temp.sort(reverse=True)
print(temp[K-1])

# [선수 지식] 최솟값 구하기
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

for x in arr:
    if x < arrMin:
        arrMin = x

# 대표값
N = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/N)
min = 2147000000
for index, value in enumerate(a):
    temp = abs(value-avg)
    if temp < min:
        min = temp
        score = value
        number = index + 1
    elif temp == min:
        if value > score:
            score = value
            number = index + 1
print(avg, number)
'''
파이썬에서의 round 는 round_half_even 방식을 택함
round_half_even은 아주 정확한 중간값일 경우 짝수 쪽으로
4.5000 -> 4
a = 67.5
a = a + 0.5
a = int(a)
print(a)
'''

# 정다면체 *
N, M = map(int, input().split())
cnt = [0]*(N+M+1)
max = -1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum = i+j
        cnt[sum] += 1
for i in range(len(cnt)):
    if cnt[i] > max and cnt[i] != 0:
        max = cnt[i]
for i in range(len(cnt)):
    if cnt[i] == max:
        print(i, end=' ')

# 자릿수의 합 *
N = int(input())
a = list(map(int, input().split()))
max = -2147000

def digit_sum(x):
    number = str(x)
    numberSum = 0
    for i in number:
        numberSum += int(i)
    return numberSum


for i in range(len(a)):
    numberSum = digit_sum(a[i])
    if numberSum > max:
        max = numberSum
        answer = a[i]
print(answer)
'''
digit함수에서 string으로 바꾸는것 이외에도
while x>0:
    sum+=x%10
    x=x//10
사용가능

아니면 
number = str(x)
for i in number:
이 부분을 
for i in str(x):
이렇게 간편하게 변경하기
'''

# 소수(에라토스테네스 체)
N = int(input())
ch = [0]*(N+1)
cnt = 0
for i in range(2, N+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            ch[j]=1
print(cnt)

# 뒤집은 소수
N = int(input())
a = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True

for x in a:
    temp = reverse(x)
    if isPrime(temp):
        print(temp, end=' ')

# 주사위 게임 *
N = int(input())
maxPrize = -21470000
for i in range(N):
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2]:
        prize = 10000 + a[0]*1000
    elif a[0] == a[1]:
        prize = 1000 + a[0]*100
    elif a[0] == a[2]:
        prize = 1000 + a[0] * 100
    elif a[1] == a[2]:
        prize = 1000 + a[1] * 100
    else:
        prize = max(a) * 100
    if prize > maxPrize:
        maxPrize = prize
print(maxPrize)

'''
max(a)를 안쓰려면
a, b, c를 
sort로 정렬을 하고
c의 값을 넣으면됨 
'''

# 점수 계산 *
N = int(input())
a = list(map(int, input().split()))
cnt = 0
score = 0
for x in a:
    if x == 1:
        cnt += 1
        score += cnt
    elif x == 0:
        cnt = 0
print(score)