# set 교집합 이용

N, M = map(int, input().split())
d = set(list(input() for _ in range(N)))
b = set(list(input() for _ in range(M)))
db = sorted(d & b)
print(len(db))

for x in db:
    print(x)
