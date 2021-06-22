def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_cnt = [0, 0, 0]
    result = []
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            answer_cnt[0] += 1
        if answers[i] == second[i % 8]:
            answer_cnt[1] += 1
        if answers[i] == third[i % 10]:
            answer_cnt[2] += 1
    for i in range(len(answer_cnt)):
        if max(answer_cnt) == answer_cnt[i]:
            result.append(i+1)
    return result