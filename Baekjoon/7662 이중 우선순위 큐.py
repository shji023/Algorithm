'''
리스트를 사용하면 시간복잡도가 너무 큼
->조회 밎 삽입의 시간이 O(1)인 맵을 사용해야함
딕셔너리(맵)에 숫자, 빈도수 형태로 값을 이용
Dequedp 숫자를 bisect.insort_left를 사용하여 오름차순으로 삽입
bisect-이진탐색 쉽게구현
bisect_left(literable, value) : 왼쪽 인덱스를 구하기
bisect_right(literable, value) : 오른쪽 인덱스를 구하기
덱에서 정렬된 숫자를 기준으로 최솟값 또는 최댓값을 제거함
'''
import sys
from collections import deque
import bisect
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    nums = dict()
    d = deque()
    k = int(input())
    for _ in range(k):
        q = input().split()
        if q[0] == 'I':
            if nums.get(int(q[1])) is None:
                nums[int(q[1])] = 1
                bisect.insort_left(d, int(q[1]))
            else:
                nums[int(q[1])] += 1
        elif q[0] == 'D' and nums:
            # 최솟값 삭제
            if q[1] == '-1':
                nums[d[0]] -= 1
                if nums[d[0]] == 0:
                    nums.pop(d[0])
                    d.popleft()
            # 최댓값 삭제
            else:
                nums[d[-1]] -= 1
                if nums[d[-1]] == 0:
                    nums.pop(d[-1])
                    d.pop()
    if d:
        result.append(str(d[-1]) + " " + str(d[0]))
    else:
        result.append("EMPTY")

for r in result:
    print(r)
