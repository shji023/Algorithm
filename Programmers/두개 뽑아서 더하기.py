def solution(numbers):
    answer = []
    temp = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp.add(numbers[i]+numbers[j])
    for i in temp:
        answer.append(i)
    answer.sort()
    return answer

# return sorted(list(set(answer)))
