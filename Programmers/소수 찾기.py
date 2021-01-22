'''
완전탐색 - 모든 경우의 수를 전부 찾아서 답을 찾는 알고리즘
완전탐색 종류
Brute Force : for문과 if문을 이용하여 처음부터 끝까지 탐색하는 방법
비트 마스크 : 이진수 표현을 자료구조로 쓰는 기법 (AND, OR, XOR, SHIFT, NOT)
재귀 함수
순열 : 서로 다른 n개의 원소에서 r개의 중복을 허용하지 않고 순서대로 늘어 놓은 수
BFS(너비우선탐색), DFS(깊이우선탐색)

이 중 DFS 방법으로 문제해결
'''

answer = 0
arr = []


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def dfs(x, numbers, graph, visited):
    global answer, arr
    size = len(numbers)
    temp = ''
    if x == size:
        for t in graph:
            temp += t
        temp = int(temp)
        arr.append(temp)
    else:
        for i in range(1, size + 1):
            if not visited[i]:
                visited[i] = True
                graph[x] = numbers[i - 1]
                dfs(x + 1, numbers, graph, visited)
                visited[i] = False


def solution(numbers):
    global answer, arr
    size = len(numbers)
    visited = [False] * (size + 1)
    graph = [0] * size
    dfs(0, numbers, graph, visited)
    arr.sort()
    answerArr = []
    answerArr.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answerArr.append(arr[i])
    for q in answerArr:
        if isPrime(q):
            answer += 1
    return answer


# 피드백

# 만들 수 있는 수를 저장하는 set(자동 중복제거)
answerArr = set()


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def dfs(cnt, numbers, snum, visited):
    size = len(numbers)
    if cnt == size and snum != "":
        answerArr.add(int(snum))
    else:
        for i in range(size):
            if not visited[i]:
                visited[i] = True
                # sum+ numbers[i] 하면서 숫자를 조합
                dfs(cnt + 1, numbers, snum + numbers[i], visited)
                visited[i] = False
        # 최종적으로 '7' 일 경우는 cnt값은 1인 채로 dfs가 종료 되는 경우
        if snum != "":
            answerArr.add(int(snum))


def solution(numbers):
    answer = 0
    size = len(numbers)
    visited = [False] * (size)
    dfs(0, numbers, "", visited)
    # 소수의 개수 구하기
    for q in answerArr:
        if isPrime(q):
            answer += 1
    return answer
