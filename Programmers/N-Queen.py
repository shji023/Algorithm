answer = 0


def check(queen, current_col):
    current_row = len(queen)
    for q in range(current_row):
        if queen[q] == current_col or abs(queen[q] - current_col) == current_row - q:
            return False
    return True


def dfs(n, current_row, queen):
    global answer
    if current_row == n:
        answer += 1
        return
    for current_col in range(n):
        if check(queen, current_col):
            queen.append(current_col)
            dfs(n, current_row + 1, queen)
            queen.pop()


def solution(n):
    dfs(n, 0, [])
    return answer


a = solution(4)
print(a)
