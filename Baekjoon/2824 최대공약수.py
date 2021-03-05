# 최대공약수 유클리드 호제법 구현 - 반복문 사용
import sys

input = sys.stdin.readline

N = int(input())
arr_A = list(map(int, input().split()))
M = int(input())
arr_B = list(map(int, input().split()))
A, B = 1, 1
for x in arr_A:
    A *= x
for y in arr_B:
    B *= y


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


answer = gcd(A, B)
if len(str(answer)) > 9:
    answer = str(answer)[len(str(answer)) - 9:]
print(answer)