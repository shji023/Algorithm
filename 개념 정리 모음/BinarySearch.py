'''
이진 탐색
탐색 범위를 반으로 좁혀가면 빠르게 탐색하는 알고리즘
순차 탐색 - 리스트 안에있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
이진 탐색 - 배열 내부의 데이터가 정렬되어 있어야함
3가지 변수 : 시작점, 끝점, 중간점
"찾으려는 데이터와 중간점 위치에 있는 데이터 반복적 비교"
한번 확인할 때마다 확인하는 원소의 개수가 대략 절반씩 감소 - O(logN)
구현 방법 1.재귀함수  2.반복문
'''
# 1
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# 2
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# input
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

'''
* 이진 탐색 트리 - 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
* 입력받기 시간초과 해결
import sys
input_data = sys.stdin.readline().rstrip()
'''