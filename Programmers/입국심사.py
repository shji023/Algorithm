def binary_search(array, people, start, end):
    ans = 0
    while start <= end:
        check = 0
        mid = (start+end)//2
        for x in array:
            check += mid//x
        '''
        n = 7 , times[3,5] 
        => 15
        15/3 = 5 , 15/5 = 3  check = 8
        몫의 합이 n보다 크거나 같은 경우 , n보다 작은 경우 
        -> 이렇게 2가지 경우로 분기해서 mid를 ans값에 기록하면서 돌려야함 
        '''
        if check >= people:
            ans = mid
            end = mid - 1
        elif check < people:
            start = mid + 1
    return ans


def solution(n, times):
    end = max(times) * n
    answer = binary_search(times, n, 0, end)
    return answer


print(solution(1, [2, 2]))