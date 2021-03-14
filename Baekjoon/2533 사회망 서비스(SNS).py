'''
DFS
문제에 있는 예시 그래프 탐색 순서 (깊이 우선으로)
1->2->5->6->3->4->7->8
최소의 얼리어답터를 고르는 기준
1. 현재 노드가 단말노드이면 연결된 노드는 얼리어답터
2. 연결된 모든 노드중에 얼리어답터가 없으면 현재 노드가 얼리어답터
'''
import sys

sys.setrecursionlimit(1000000)
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
ea = set()
visited = set()

# 양방향으로 그래프 만들어주기
for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# dfs
def check(n):
    global graph, ea, visited
    visited.add(n)
    # 단말 노드일 경우
    if len(graph[n]) == 1:
        return True
    for i in graph[n]:
        # 이 문장 없으면 갔던 곳 또 방문, 재귀 안끝남
        if i not in visited:
            # 조건1.
            if check(i):
                ea.add(n)
            # 조건2.
            elif i not in ea:
                ea.add(n)
    return False


# 처음부터 단말노드가 들어가면 바로 true 반환하기 때문에 틀림
for t in range(1, N + 1):
    if len(graph[t]) > 1:
        check(t)
        break
# N이 1이거나 2이면 들어가면 바로 true 반환하기 때문에 ea값 없음
if N > 2:
    print(len(ea))
else:
    print(1)
