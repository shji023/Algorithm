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

def solution(answers):
    answer = []
    f_cnt, s_cnt, t_cnt = 0, 0, 0
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            f_cnt += 1
        if answers[i] == second[i%8]:
            s_cnt += 1
        if answers[i] == third[i%10]:
            t_cnt += 1
    Max = max(f_cnt, s_cnt, t_cnt)
    if Max == f_cnt:
        answer.append(1)
    if Max == s_cnt:
        answer.append(2)
    if Max == t_cnt:
        answer.append(3)
    return answer
