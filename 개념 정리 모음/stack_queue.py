# 스택
# First In Last Out
# 파이썬에선 스택을 이용할 때 별도의 라이브러리 사용할 필요가 없음
# 기본 list에서 append와 pop이용하면 스택 자료구조와 동일하게 동작
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
# [5,2,3,1]
print(stack)
# [1,3,2,5]
print(stack[::-1])

# 큐
# First In First Out
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

#deque([3,7,1,4])
print(queue)
queue.reverse()
#deque([4,1,7,3])
print(queue)

