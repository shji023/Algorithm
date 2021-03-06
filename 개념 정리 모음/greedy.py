'''
그리디(greedy)알고리즘, 탐욕법
'현재 상황에서 지금 당장 좋은 것만 고르는 방법'
특정한 문제를 만났을 때, 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있는 지 파악할 수 있어야함
'''

# 대표 예제 - 거스름돈
n = 1260
cnt = 0

coin_types = [500, 100, 50, 10]
for coin in coin_types:
    cnt += n // coin
    n %= coin
print(cnt)

'''
화폐의 종류가 K일 경우 코드의 시간 복잡도 O(K)
거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유
<가지고 있는 동전 중에서는 큰 단위가 항상 작은 단위의 배구 이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문>
동전의 단위가 서로 배수의 형태가 아니라 무작위로 주어진 경우에는 그리디 알고리즘으로 해결 불가능 
'''