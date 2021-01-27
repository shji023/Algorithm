'''
- 오름차순으로 알파벳을 정렬한다
- 선택한 알파벳 기준으로 오른쪽 범위 의 알파벳을 순회 한다
- 만들어진 알파벳 조합에서 모음과 자음의 개수가 유효한지 검사한다
'''

L, C = map(int, input().split())
array = list(input().split())
array.sort()
result = []


def dfs(current_idx, password):
    # 현재 인덱스가 L의 길이와 같다면 result에 추가하기
    if len(password) == L:
        result.append(password[:])
        return
    # array에 있는 알파벳들 돌면서 적합한지 체크
    for i in range(current_idx, len(array)):
        password.append(array[i])
        # 오름 차순으로 설정해놓고 DFS를 돌리고 DFS 함수 내부의 for문의 시작 인덱스를 이전 dfs에서 선택한 문자
        # index+1로 설정하면 그 이전의 알파벳을 선택할 경우가 없을 것
        # —> 이거 자체로 제외 조건이 설정된거여서 굳이체킹할 필요 없음
        dfs(i + 1, password)
        password.pop()


def is_available(result):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for r in result:
        mo, ja = 1, 2
        for j in r:
            if j in vowel:
                mo -= 1
            else:
                ja -= 1
        if mo <= 0 and ja <= 0:
            for x in r:
                print(x, end='')
            print()
    return


dfs(0, [])
is_available(result)