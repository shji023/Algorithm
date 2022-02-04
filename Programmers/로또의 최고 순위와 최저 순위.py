def solution(lottos, win_nums):
    answer = []
    same = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                same += 1
    maxSame = same + lottos.count(0)
    if same < 2:
        answer.append(6)
    elif same == 2:
        answer.append(5)
    elif same == 3:
        answer.append(4)
    elif same == 4:
        answer.append(3)
    elif same == 5:
        answer.append(2)
    elif same == 6:
        answer.append(1)

    if maxSame < 2:
        answer.append(6)
    elif maxSame == 2:
        answer.append(5)
    elif maxSame == 3:
        answer.append(4)
    elif maxSame == 4:
        answer.append(3)
    elif maxSame == 5:
        answer.append(2)
    elif maxSame == 6:
        answer.append(1)        
    return sorted(answer)
