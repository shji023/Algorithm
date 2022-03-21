# 적은 예산순으로 넣어야 많이 나눠줄 수 있음 - 오름차순으로 정렬하기
def solution(d, budget):
    answer = 0
    newD = sorted(d)
    for i in range(len(newD)):
        if budget >= newD[i]:
            budget -= newD[i]
            answer += 1
        else:
            break
    return answer