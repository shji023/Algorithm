'''
트라이(Trie) 자료구조
문자열 집합을 표현하는 트리 자료구조
시간 복잡도 - O(n)
루트 노드가 되는 가장 최상위 노드에는 아무단어도 들어가지 않음
루트 아래 노드부터 문자열들의 접두사가 나타남
ex) apple
a->ap->app->appl->apple
모두 apple의 접두사
=> 시간 복잡도는 문자열 길이만큼
공간 복잡도에서 비효율적
'''
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


class Node():
    def __init__(self, key):
        self.key = key
        self.children = dict()


class Trie():
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]

    # 구조 출력
    def printStructure(self, cnt, curr_node):
        # 가장 아래에 있는 노드
        if cnt == 0:
            curr_node = self.head

        for char in sorted(curr_node.children.keys()):
            print('--'*cnt, char, sep='')
            self.printStructure(cnt+1, curr_node.children[char])


trie = Trie()

N = int(input())

for _ in range(N):
    arr = list(input().split())
    trie.insert(arr[1:])

trie.printStructure(0, None)