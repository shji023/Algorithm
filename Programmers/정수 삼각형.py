# 실패 코드
# 현재 d[i]를 선택할 때 두가지의 경우의 수 중에서 다음 수와 더하여 가장 큰수를 가질 수 잇는 경우를 현재의 d[i]으로 채택한다.
# 다음 수와 더해서 경우의 수는 4개 -> one two three four
# d[i] = d[i-1] + triangle[i][?]
# 다음 행으로 갈때 현재의 j위치를 기억하여 사용
def solution(triangle):
    answer = 0
    d = [0] * 500
    d[0] = triangle[0][0]
    saveJ = 0
    for i in range(1, len(triangle)):
        j = saveJ
        if i < len(triangle) - 1:
            array = []
            one = d[i - 1] + triangle[i][j] + triangle[i + 1][j]
            two = d[i - 1] + triangle[i][j] + triangle[i + 1][j + 1]
            three = d[i - 1] + triangle[i][j + 1] + triangle[i + 1][j + 1]
            four = d[i - 1] + triangle[i][j + 1] + triangle[i + 1][j + 2]
            array.append(one)
            array.append(two)
            array.append(three)
            array.append(four)
            if max(array) == one or two:
                d[i] = d[i - 1] + triangle[i][j]
                saveJ = j
            elif max(array) == two:
                d[i] = d[i - 1] + triangle[i][j]
                saveJ = j
            elif max(array) == three:
                d[i] = d[i - 1] + triangle[i][j + 1]
                saveJ = j + 1
            elif max(array) == four:
                d[i] = d[i - 1] + triangle[i][j + 1]
                saveJ = j + 1
        else:
            d[i] = max(d[i - 1] + triangle[i][j], d[i - 1] + triangle[i][j + 1])

    answer += d[len(triangle) - 1]
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
a = solution(triangle)
print(a)


# 정답 코드


def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    return max(triangle[-1])
