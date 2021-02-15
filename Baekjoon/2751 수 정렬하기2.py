import sys
input = sys.stdin.readline
N = int(input())
a = list(int(input())for _ in range(N))
a.sort()
for x in a:
    print(x)

'''
시간초과
import sys
input = sys.stdin.readline

N = int(input())
a = list(int(input()) for _ in range(N))


def qsort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] < arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    qsort(arr, start, right - 1)
    qsort(arr, right + 1, end)


qsort(a, 0, N - 1)
for x in a:
    print(x)
'''

