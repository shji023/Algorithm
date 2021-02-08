'''
슬라이딩 윈도우 예시
연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 수를 합한 값을 구하는 문제
여러번 사용될 만한 정보는 미리 구해 저장 해놓기
매번 처리되는 중복된 요소를 버리지 않고 재사용함으로써 낭비되는 계산을 하지 않음으로써 효율적으로 처리하는 방법
투 포인터 알고리즘 같은 경우 left와 right라는 처음과 끝을 가리키는 포인터가 서로 독립적으로 움직이는데에 반해,
슬라이딩 윈도우 알고리즘은 처음과 끝을 가리키는 포인터가 서로 같이 움직인다.(고정된 윈도우가 슬라이딩 하는 것처럼)
제한된 메모리 or 길이 or 구간 등이 있다는 점이 특징
주로 Deque이용
'''
# 제한된 메모리 안에서 코드를 작성하는 문제
# dp + 슬라이딩 윈도우 유형의 문제여서 dp식으로 계산하지만 dp배열처럼 누적된 전체 값은 필요 없으므로,
# 한 행만 기록하여 메모리를 초과하지 않도록 작성한다
# a 값 변경되지 않도록 깊은 복사
import sys
import copy
input = sys.stdin.readline
N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    if i == 0:
        Max = copy.deepcopy(a)
        Min = copy.deepcopy(a)
    else:
        Max[0], Max[1], Max[2] = max(Max[0], Max[1]) + a[0],\
                                 max(Max) + a[1],\
                                 max(Max[1], Max[2]) + a[2]
        Min[0], Min[1], Min[2] = min(Min[0], Min[1]) + a[0], \
                                 min(Min) + a[1], \
                                 min(Min[1], Min[2]) + a[2]
print(max(Max), min(Min))

'''
Max[0] = max(Max[0], Max[1]) + a[0]
Max[1] = max(Max) + a[1]
Max[2] = max(Max[1], Max[2]) + a[2]

Min[0] = min(Min[0], Min[1]) + a[0]
Min[1] = min(Min) + a[1]
Min[2] = min(Min[1], Min[2]) + a[2]
이렇게 할 경우 Max값이 실시간으로 바뀜
'''