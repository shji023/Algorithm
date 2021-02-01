def solution(n):
    answer = []
    array = [[0 for _ in range(x)] for x in range(1, n+1)]
    x = -1
    y = 0
    num = 1
    for i in range(0, n):
        for j in range(n-i, 0, -1):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            array[x][y] = num
            num += 1
    for t in array:
        for r in t:
            answer.append(r)
    return answer

solution(4)