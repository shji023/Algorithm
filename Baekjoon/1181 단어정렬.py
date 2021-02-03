N = int(input())
array = []
for i in range(N):
    a = input()
    array.append((len(a), a))
array = list(set(array))
array.sort()
for j in array:
    print(j[1])