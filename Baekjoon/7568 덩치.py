# 이중 포문 돌려 전체 다 비교, 나보다 덩치 큰 사람이 있을 경우 rank+=1
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")

