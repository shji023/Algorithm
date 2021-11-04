n = int(input())
arr = list(map(int, input().split()))
idx = list(i for i in range(1, n+1))

v = arr.pop(0)
idx.pop(0)

temp = 0
result = [1]

while arr:
    if v > 0:
        v -= 1
        temp = (temp + v) % len(arr)
    elif v < 0:
        temp = (temp + v) % len(arr)

    v = arr.pop(temp)
    q = idx.pop(temp)
    result.append(q)

for i in result:
    print(i, end=' ')