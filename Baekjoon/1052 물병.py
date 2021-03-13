import sys

input = sys.stdin.readline
N, K = map(int, input().split())


def bottle(N):
    cnt = 0
    while True:
        quotient = N // 2
        remainder = N % 2
        cnt += remainder
        N = quotient
        if N == 0:
            break
    return cnt


if N > K:
    temp = N
    while True:
        if bottle(temp) <= K:
            print(temp - N)
            break
        else:
            temp += 1
else:
    print(0)