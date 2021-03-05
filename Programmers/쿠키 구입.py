import sys

input = sys.stdin.readline


def solution(cookie):
    answer = 0
    N = len(cookie)
    # 반복문으로 인덱스값 하나씩 증가하면서
    for idx in range(N - 1):
        # 현재 인덱스 기준으로 오른쪽 왼쪽 나눔
        left, right = idx, idx + 1
        # 오른쪽 왼쪽 쿠키
        l_cookie, r_cookie = cookie[left], cookie[right]
        while left > -1 and right < N:
            if l_cookie == r_cookie:
                answer = max(answer, l_cookie)
            if l_cookie < r_cookie:
                left -= 1
                if left > -1:
                    l_cookie += cookie[left]
            else:
                right += 1
                if right < N:
                    r_cookie += cookie[right]
    return answer
