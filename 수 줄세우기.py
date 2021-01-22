'''
정수 n을 입력 받는다  (1<n<5)
1부터 n까지의 수를 줄세우는 모든 방법을 반환하는 함수를 DFS로 구현 하시오.

ex) n = 3 일경우

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
으로 총 6 가지 의 경우의 수가 있다

입력 :3
출력 :6
'''

def dfs(graph, x, visited):
    global cnt
    if x == n:
        cnt += 1
    else:
        # 방문안햇을때만 true 로 바꿔줌
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                # 하나씩 증가
                dfs(graph, x + 1, visited)
                # 방문 완료했으면 다시 false로 바꿔줌
                visited[i] = False


n = int(input())
cnt = 0
graph = [0] * n
# 방문된 정보 배열 false로 초기화
visited = [False] * (n + 1)
dfs(graph, 0, visited)
print(cnt)