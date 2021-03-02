def dfs(x, sum, numbers, target):
    global answer

    if x == len(numbers):
        if sum == target:
            answer += 1
    else:
        dfs(x + 1, sum + numbers[x], numbers, target)
        dfs(x + 1, sum - numbers[x], numbers, target)
    return answer


def solution(numbers, target):
    global answer

    answer = 0
    dfs(0, 0, numbers, target)
    return answer