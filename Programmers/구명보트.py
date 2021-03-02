'''
에러 코드
1. 보트에 두명만 탈 수 있다는 것을 고려x
2. 첫번째 부터 태우고 나머지 중 무게 들어갈 수 있는 거 더 태우는 방식으로 함

def solution(people, limit):
    answer = 0
    sumP = 0
    for p in people:
        sumP += p
    for i in range(len(people)):
        tempLimit = limit - people[i]
        sumP = sumP - people[i]
        print(sumP, tempLimit)
        for j in range(i+1, len(people)):
            if people[j] > tempLimit:
                continue
            else:
                tempLimit = tempLimit - people[j]
                sumP = sumP - people[j]
                # 같은 보트에 타는 것은 맞지만 tempLimit과 sumP이 0이 아닌경우 고려 x
                if tempLimit == 0 or sumP == 0:
                    answer += 1
        if tempLimit == limit-people[i]:
            answer += 1
        if sumP == 0:
            break
    return answer

people = [70,80,50]
limit = 100
an = solution(people, limit)
print(an)
'''


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people)-1
    while start <= end:
        if people[start]+people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
        else:
            start += 1
            answer += 1
    return answer
