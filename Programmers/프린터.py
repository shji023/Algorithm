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

# 다른 방법
def solution(pri, location):
    cnt = 0
    while True:
        Max = max(pri)
        v = pri.pop(0)
        if v >= Max:
            if location == 0:
                cnt += 1
                return cnt
                break
            else:
                cnt += 1
                if location == 0:
                    location = len(pri) - 1
                else:
                    location -= 1
        else:
            pri.append(v)
            if location == 0:
                location = len(pri) - 1
            else:
                location -= 1