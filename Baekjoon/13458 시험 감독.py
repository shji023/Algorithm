import sys

input = sys.stdin.readline

n = int(input())
e = list(map(int, input().split()))
s = list(map(int, input().split()))
cnt = 0
for x in e:
    x = x - s[0]
    cnt += 1
    if x > 0:
        cnt += x // s[1]
        if x % s[1] > 0:
            cnt += 1
print(cnt)
