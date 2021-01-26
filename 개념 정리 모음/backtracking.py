'''
백트래킹의 원리
1. 어떤 노드의 유망성을 점검 후,
2. 유망하지 않으면 배제시킨다. = 가지치기
3. 해당 노드의 부모노드로 되돌아간 후 다른 자손노드를 검색한다. → 풀이시간 단축

구현 시, 고려할 수 있는 모든 경우의 수를 상태공간트리를 통해 표현
경우의 수를 탐색하는 방식에 가장 적합한 것 - DFS
'''


def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


solve_n_queens(4)
# [[1, 3, 0, 2], [2, 0, 3, 1]]
