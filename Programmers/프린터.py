from collections import deque

def solution(priorities, location):
    deq = deque([])
    deqPri = deque(priorities)
    for i in range(len(priorities)):
        deq.append((i, priorities[i]))
    cnt = 0
    while True:
        if deq[0][1] >= max(deqPri):
            cnt += 1
            if deq[0][0] == location:
                answer = cnt
                break
            deq.popleft()
            deqPri.popleft()
        else:
            deq.append(deq[0])
            deq.popleft()
            deqPri.append(deqPri[0])
            deqPri.popleft()
    return answer