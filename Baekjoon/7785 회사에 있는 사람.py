# set 관련 함수 이용

n = int(input())
people = set([])
arr = []

for i in range(n):
    log = input().split()
    if log[1] == 'enter':
        people.add(log[0])
    else:
        people.remove(log[0])

for x in people:
    arr.append(x)
arr.sort(reverse=True)

for y in arr:
    print(y)