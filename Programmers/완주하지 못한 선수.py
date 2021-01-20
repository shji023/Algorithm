def solution(participant, completion):
    answer = ''
    # 알파벳 순서대로 정렬
    participant.sort()
    completion.sort()
    # 반복문을 통해 두개의 리스트 비교, 만약 다른 데이터가 있으면 그 값 answer에 넣기, 다른 데이터가 없으면 참가자의 마지막 값 넣기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = str(participant[i])
            break
    else:
        answer = str(participant[len(participant)-1])
    return answer

# 해시로 풀기 (참조한 코드)

def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    # 원소 hash()를 적용해 값을 얻어 딕셔너리의 키로 할당, 원소 값을 value로 할당
    # temp에 participant의 key 값 다 더함
    # 다 더한 temp에서 completion을 돌면서 key값을 하나씩 빼기
    # 남은 temp 값이 완주하지 못한 선수의 key 값
    # 해당 key값을 dic에서 찾아 answer에 할당
    for x in participant:
        dic[hash(x)] = x
        temp += hash(x)
    for y in completion:
        temp -= hash(y)
    answer = dic[temp]
    return answer
