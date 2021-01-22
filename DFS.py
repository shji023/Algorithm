'''
탐색(Search) :  많은 양의 데이터 중 원하는 데이터를 찾는 과정을 의미
DFS(Depth-First-Search)
깊이 우선 탐색
stack(혹은 재귀함수)이용
1. 탐색 시작 노드 스택에 삽임, 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 있을시, 그 노드 스택에 넣고 방문처리.
방문하지 않은 인접 노드 없을시, 스택에서 최상단 노드 꺼냄
3. 2번의 과정 수행할 수 없을 때 까지 반복
'''


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False]*9
dfs(graph, 1, visited)