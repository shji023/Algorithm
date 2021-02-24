'''
서로소 집합 - 공통 원소가 없는 두 집합
서로소 집합 자료구조 - 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
union, find 연산
union : 2개의 원소가 포함된 집합을 하나의 집합으로 합침
find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
=>union-find 자료구조
1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    a. A와 B의 루트 노드 A', B'를 각각 찾는다.
    b. A'를 B'의 부모 노드로 설정한다.(B'가 A'를 가리키도록 한다)
2. 모든 union 연산을 처리할 때까지 1번 과정을 반복한다.
'''
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
원소가 모두 같은 집합에 속하는 경우,노드의 개수가 N, find 혹은 union 연산의 개수가 M이면 시간복잡도 O(VM)이 되어 비효율적
경로 압축(Path Compression)기법 적용
'''

# 기존 find 함수 수정
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 부모 테이블의 원소가 최상위 노드로 다 변경됨