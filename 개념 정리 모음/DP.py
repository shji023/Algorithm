"""
<다이나믹 프로그래밍 - 동적계획법>
메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있는 방법
방식
1. Top-Down
2. Bottom-Up
"""


# 피보나치 함수 코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

'''
다이나믹 프로그래밍을 사용할 수 있는 조건
1. 최적 부분 구조 
   큰 문제를 작은 문제로 나눌 수 있다. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
2. 중복되는 부분 문제
   동일한 작은 문제를 반복적으로 해결해야함
'''
# Memoization 기법 사용(Top-Down 방식)
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))

# 반복문 사용(Bottom-Up 방식)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

'''
큰 문제를 작게 나누고, 같은 문제라면 한번씩만 풀어 문제를 효율적으로 해결하는 알고리즘
퀵정렬 - 큰 문제를 작게 나눔 (정렬을 수행할 때 리스트를 분할하며 전체적으로 정렬) =>분할 정복
분할정복과 dp 공통점 : 최적 부분 구조
분할정복과 dp 차이점 : 부분 문제의 중복
퀵 - 피벗의 위치를 잡게 되면 그 피벗값을 다시 처리하지 않음
dp - 이미 해결된 부분 문제에 대한 답 저장, 이미 해결 됐던 것이니까 다시 해결할 필요 없겠다를 반환
'''
