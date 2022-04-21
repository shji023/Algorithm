# 시계 방향일 때 반시계 방향일때
# 번호가 1, 2, 3, 4일때
# if문 다돌림
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

def counterclockwise(rotate_arr):
    temp = rotate_arr[0]
    for i in range(1, len(rotate_arr)):
        rotate_arr[i-1] = rotate_arr[i]
    rotate_arr[len(rotate_arr)-1] = temp
    return rotate_arr

def clockwise(rotate_arr):
    temp = rotate_arr[len(rotate_arr)-1]
    for i in range(len(rotate_arr)-1, 0, -1):
        rotate_arr[i] = rotate_arr[i-1]
    rotate_arr[0] = temp
    return rotate_arr

arr = [list(input().rstrip()) for _ in range(4)]
N = int(input())
for _ in range(N):
    number, direction = map(int, input().split())
    line = []
    line.append(arr[0][2])
    line.append(arr[1][6])
    line.append(arr[1][2])
    line.append(arr[2][6])
    line.append(arr[2][2])
    line.append(arr[3][6])
    # 반시계 방향
    if direction == -1:
        if number == 1:
            # 다르면
            if line[0] != line[1]:
                if line[2] != line[3]:
                    if line[4] != line[5]:
                        arr[0] = counterclockwise(arr[0])
                        arr[1] = clockwise(arr[1])
                        arr[2] = counterclockwise(arr[2])
                        arr[3] = clockwise(arr[3])
                    else:
                        arr[0] = counterclockwise(arr[0])
                        arr[1] = clockwise(arr[1])
                        arr[2] = counterclockwise(arr[2])
                else:
                    arr[0] = counterclockwise(arr[0])
                    arr[1] = clockwise(arr[1])
            else:
                arr[0] = counterclockwise(arr[0])
        elif number == 2:
            if line[0] != line[1]:
                if line[2] != line[3]:
                    if line[4] != line[5]:
                        arr[1] = counterclockwise(arr[1])
                        arr[0] = clockwise(arr[0])
                        arr[2] = clockwise(arr[2])
                        arr[3] = counterclockwise(arr[3])
                    else:
                        arr[1] = counterclockwise(arr[1])
                        arr[0] = clockwise(arr[0])
                        arr[2] = clockwise(arr[2])
                else:
                    arr[1] = counterclockwise(arr[1])
                    arr[0] = clockwise(arr[0])
            else:
                if line[2] != line[3]:
                    if line[4] != line[5]:
                        arr[1] = counterclockwise(arr[1])
                        arr[2] = clockwise(arr[2])
                        arr[3] = counterclockwise(arr[3])
                    else:
                        arr[1] = counterclockwise(arr[1])
                        arr[2] = clockwise(arr[2])
                else:
                    arr[1] = counterclockwise(arr[1])
        elif number == 3:
            if line[4] != line[5]:
                if line[2] != line[3]:
                    if line[0] != line[1]:
                        arr[2] = counterclockwise(arr[2])
                        arr[3] = clockwise(arr[3])
                        arr[1] = clockwise(arr[1])
                        arr[0] = counterclockwise(arr[0])
                    else:
                        arr[2] = counterclockwise(arr[2])
                        arr[3] = clockwise(arr[3])
                        arr[1] = clockwise(arr[1])
                else:
                    arr[2] = counterclockwise(arr[2])
                    arr[3] = clockwise(arr[3])
            else:
                if line[2] != line[3]:
                    if line[0] != line[1]:
                        arr[2] = counterclockwise(arr[2])
                        arr[1] = clockwise(arr[1])
                        arr[0] = counterclockwise(arr[0])
                    else:
                        arr[2] = counterclockwise(arr[2])
                        arr[1] = clockwise(arr[1])
                else:
                    arr[2] = counterclockwise(arr[2])
        elif number == 4:
            if line[4] != line[5]:
                if line[2] != line[3]:
                    if line[0] != line[1]:
                        arr[3] = counterclockwise(arr[3])
                        arr[2] = clockwise(arr[2])
                        arr[1] = counterclockwise(arr[1])
                        arr[0] = clockwise(arr[0])
                    else:
                        arr[3] = counterclockwise(arr[3])
                        arr[2] = clockwise(arr[2])
                        arr[1] = counterclockwise(arr[1])
                else:
                    arr[3] = counterclockwise(arr[3])
                    arr[2] = clockwise(arr[2])
            else:
                arr[3] = counterclockwise(arr[3])
    # 시계방향
    else:
        if number == 1:
            if line[0] != line[1]:
                if line[2] != line[3]:
                    if line[4] != line[5]:
                        arr[0] = clockwise(arr[0])
                        arr[1] = counterclockwise(arr[1])
                        arr[2] = clockwise(arr[2])
                        arr[3] = counterclockwise(arr[3])
                    else:
                        arr[0] = clockwise(arr[0])
                        arr[1] = counterclockwise(arr[1])
                        arr[2] = clockwise(arr[2])
                else:
                    arr[0] = clockwise(arr[0])
                    arr[1] = counterclockwise(arr[1])
            else:
                arr[0] = clockwise(arr[0])
        elif number == 2:
            if line[0] != line[1]:
                if line[2] != line[3]:
                    if line[4] != line[5]:
                        arr[1] = clockwise(arr[1])
                        arr[0] = counterclockwise(arr[0])
                        arr[2] = counterclockwise(arr[2])
                        arr[3] = clockwise(arr[3])
                    else:
                        arr[1] = clockwise(arr[1])
                        arr[0] = counterclockwise(arr[0])
                        arr[2] = counterclockwise(arr[2])
                else:
                    arr[1] = clockwise(arr[1])
                    arr[0] = counterclockwise(arr[0])
            else:
                if line[2] != line[3]:
                    if line[4] != line[5]:
                        arr[1] = clockwise(arr[1])
                        arr[2] = counterclockwise(arr[2])
                        arr[3] = clockwise(arr[3])
                    else:
                        arr[1] = clockwise(arr[1])
                        arr[2] = counterclockwise(arr[2])
                else:
                    arr[1] = clockwise(arr[1])
        elif number == 3:
            if line[4] != line[5]:
                if line[2] != line[3]:
                    if line[0] != line[1]:
                        arr[2] = clockwise(arr[2])
                        arr[3] = counterclockwise(arr[3])
                        arr[1] = counterclockwise(arr[1])
                        arr[0] = clockwise(arr[0])
                    else:
                        arr[2] = clockwise(arr[2])
                        arr[3] = counterclockwise(arr[3])
                        arr[1] = counterclockwise(arr[1])
                else:
                    arr[2] = clockwise(arr[2])
                    arr[3] = counterclockwise(arr[3])
            else:
                if line[2] != line[3]:
                    if line[0] != line[1]:
                        arr[2] = clockwise(arr[2])
                        arr[1] = counterclockwise(arr[1])
                        arr[0] = clockwise(arr[0])
                    else:
                        arr[2] = clockwise(arr[2])
                        arr[1] = counterclockwise(arr[1])
                else:
                    arr[2] = clockwise(arr[2])
        elif number == 4:
            if line[4] != line[5]:
                if line[2] != line[3]:
                    if line[0] != line[1]:
                        arr[3] = clockwise(arr[3])
                        arr[2] = counterclockwise(arr[2])
                        arr[1] = clockwise(arr[1])
                        arr[0] = counterclockwise(arr[0])
                    else:
                        arr[3] = clockwise(arr[3])
                        arr[2] = counterclockwise(arr[2])
                        arr[1] = clockwise(arr[1])
                else:
                    arr[3] = clockwise(arr[3])
                    arr[2] = counterclockwise(arr[2])
            else:
                arr[3] = clockwise(arr[3])
answer = 0
if arr[0][0] == '1':
    answer += 1
if arr[1][0] == '1':
    answer += 2
if arr[2][0] == '1':
    answer += 4
if arr[3][0] == '1':
    answer += 8

print(answer)


# 다른 풀이
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

# 톱니바퀴 deque에 넣는다
circle = [deque(map(int, input().rstrip())) for _ in range(4)]
N = int(input())
opers = deque(list(map(int, input().split())) for _ in range(N))

# 명령어가 남아있으면 반복문 실행
while opers:
    number, direction = opers.popleft()
    number -= 1
    # deque는 rotate가능
    # rotate(num) >> num만큼 회전 (양수:오른쪽, 음수:왼쪽)
    tmp_2 = circle[number][2]
    tmp_6 = circle[number][6]
    circle[number].rotate(direction)
    # 왜 저장할까
    # 뒤에서 어떻게 바뀌어 있을지 모르니까 처음값 저장해두는것
    tmp_direction = direction


    # 시작에서 왼쪽으로
    direction = tmp_direction
    for i in range(number-1, -1, -1):
        # 다르면
        if circle[i][2] != tmp_6:
            tmp_6 = circle[i][6]
            circle[i].rotate(direction*-1)
            direction *= -1
        else:
            break

    # 시작에서 오른쪽으로
    direction = tmp_direction
    for i in range(number+1,4):
        if circle[i][6] != tmp_2:
            tmp_2 = circle[i][2]
            circle[i].rotate(direction*-1)
            direction*=-1
        else:
            break
answer = 0
for i in range(4):
    if circle[i][0] == 1:
        answer += (2**i)
print(answer)