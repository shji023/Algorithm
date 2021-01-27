'''
백트래킹의 원리
1. 어떤 노드의 유망성을 점검 후,
2. 유망하지 않으면 배제시킨다. = 가지치기
3. 해당 노드의 부모노드로 되돌아간 후 다른 자손노드를 검색한다. → 풀이시간 단축

구현 시, 고려할 수 있는 모든 경우의 수를 상태공간트리를 통해 표현
경우의 수를 탐색하는 방식에 가장 적합한 것 - DFS
'''


def is_available(candidate, current_col):
    # 현재 행은 지금까지 배치된 퀸의 조합인 길이와 동일
    current_row = len(candidate)
    for queen_row in range(current_row):
        # 지금까지 배치된 queen들의 col 과 현재 col이 같으면 안됨/ 수직배치 체크
        # (지금까지 배치된 queen들의 col)-(현재 col)의 절대값(-가 나올수도 있으므로)과
        # (현재 row)와 (queen행)의 차(현재행이 항상 크므로 항상 양수)가 같으면 안됨/ 대각선 배치 체크
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


# current_row 한행을 처리하고 다음 행을 재귀적으로 호출
# current_candidate 현재 퀸이 배치된 정보
def DFS(N, current_row, current_candidate, final_result):
    # 배치가 다 끝났다면
    if current_row == N:
        # final_result에 지금까지의 배치 추가
        final_result.append(current_candidate[:])
        return
    # 특정 행에 N개의 열이 있음 하나 하나 체크해 나감
    for candidate_col in range(N):
        # is_available 체크하는 함수/ 이미 기존에 배치된 퀸의 정보/ 체크해야 하는 열의 번호
        if is_available(current_candidate, candidate_col):
            # 조건이 만족이 되면 current_candidate에 넣어줌
            current_candidate.append(candidate_col)
            # 그 다음행을 재귀적으로 호출/ 행+1 / 지금까지의 퀸 배치
            DFS(N, current_row + 1, current_candidate, final_result)
            # 조건에 충족하지 않는다면 백트래킹 해야함/ current_candidate에서 빼줌
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


solve_n_queens(4)
# [[1, 3, 0, 2], [2, 0, 3, 1]]
