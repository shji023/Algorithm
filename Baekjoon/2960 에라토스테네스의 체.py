N, K = map(int, input().split())
array = [0] * (N+1)
answer = []
for i in range(2, N+1):
    if array[i] == 0:
        for j in range(i, N+1, i):
            if array[j] != 1:
                array[j] = 1
                answer.append(j)
print(answer[K-1])