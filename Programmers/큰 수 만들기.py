# 런타임 에러
def solution(number, k):
    size = len(number) - k
    start = 0
    answer = ''
    # k를 제외하고 만들 수 있는 숫자 자릿수만큼
    for i in range(size):
        max = number[start]
        idx = start
        # 전체 number 배열 0~k+i
        for j in range(start, k+i+1):
            if max < number[j]:
                max = number[j]
                idx = j
        start = idx +1
        answer += str(max)
    return answer

# stack을 이용한 풀이
def solution(number, k):
    answer = ''
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()  # 뒤부터 삭제
            k -= 1

        stack.append(number[i])
    while k > 0:
        stack.pop()
        k -= 1
    answer = ''.join(stack)

    return answer
