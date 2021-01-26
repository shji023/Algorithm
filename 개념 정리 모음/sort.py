# 선택 정렬(selection sort)
'''
"가장 작은 데이터"를 선택해 "맨앞에 있는 데이터"와 바꾸고,
"그다음 작은 데이터"를 선택해 "앞에서 두번째" 데이터와 바꾸는 과정을 반복

선택 정렬의 시간복잡도 O(N^2)
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입 정렬(insertion sort)
'''
데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
(데이터가 거의 정렬되어 있을 때 훨씬 효율적)
(특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정)
자기보다 작은 데이터를 만났다면 그 자리에 데이터 삽입

삽입 정렬의 시간복잡도 O(N^2) 최선의 경우 O(N) 가능(데이터가 거의 정렬되어 있을 시)
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)

# 퀵 정렬(quick sort)
'''
기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
빠른 알고리즘(견줄만한 알고리즘 - 병합정렬)
퀵 정렬의 평균적 시간 복잡도(NlogN), 최악의 경우 (N^2)
데이터가 이미 정렬되어 있는 경우에는 매우 느리게 동작한다.
'''
# 1
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# 2
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
