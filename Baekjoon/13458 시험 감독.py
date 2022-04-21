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

# 다시 풀기
N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(len(arr)):
    arr[i] = arr[i]-B
    cnt += 1
    if arr[i] > 0:
        if arr[i] % C > 0:
            cnt += (arr[i]//C)+1
        else:
            cnt += (arr[i] // C)
print(cnt)