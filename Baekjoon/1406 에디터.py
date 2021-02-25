import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = []
M = int(input())
# cursor = len(s1)
for _ in range(M):
    command = input().split()
    if command[0] == 'P':
        s1.append(command[1])
    elif command[0] == 'L' and s1 != []:
        s2.append(s1.pop())
    elif command[0] == 'D' and s2 != []:
        s1.append(s2.pop())
    elif command[0] == 'B' and s1 != []:
        s1.pop()
result = "".join(s1)
result2 = "".join(reversed(s2))
print(result+result2)
# print("".join(s1+list(reversed(s2))))