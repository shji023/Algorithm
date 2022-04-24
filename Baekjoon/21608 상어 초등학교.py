import sys
from collections import deque
sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
classroom = [[0]*N for _ in range(N)]
info = deque([])
for i in range(N*N):
    student, o1, o2, o3, o4 = list(map(int,input().split()))
    info.append([student, o1, o2, o3, o4])
    condition1_arr = [[0] * N for _ in range(N)]
    condition2_arr = [[0] * N for _ in range(N)]
    # 1번, 2번
    for x in range(N):
        for y in range(N):
            if classroom[x][y] == 0:
                condition1_cnt = 0
                condition2_cnt = 0
                for j in range(4):
                    nx = dx[j] + x
                    ny = dy[j] + y
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if classroom[nx][ny] == o1:
                        condition1_cnt += 1
                    if classroom[nx][ny] == o2:
                        condition1_cnt += 1
                    if classroom[nx][ny] == o3:
                        condition1_cnt += 1
                    if classroom[nx][ny] == o4:
                        condition1_cnt += 1
                    if classroom[nx][ny] == 0:
                        condition2_cnt += 1
                condition1_arr[x][y] = condition1_cnt
                condition2_arr[x][y] = condition2_cnt
    condition1_max = 0
    condition2_max = 0
    condition1_list = deque([])
    condition2_list = deque([])
    for a in range(N):
        for b in range(N):
            if classroom[a][b] != 0:
                continue
            if condition1_max < condition1_arr[a][b]:
                condition1_max = condition1_arr[a][b]
                while condition1_list:
                    condition1_list.popleft()
                condition1_list.append((a, b))
            elif condition1_max == condition1_arr[a][b]:
                condition1_list.append((a, b))
    if len(condition1_list) > 1:
        for c in range(len(condition1_list)):
            d = condition1_list[c][0]
            e = condition1_list[c][1]
            if condition2_max < condition2_arr[d][e]:
                condition2_max = condition2_arr[d][e]
                if condition2_list:
                    condition2_list.popleft()
                condition2_list.append((d, e))
            elif condition2_max == condition2_arr[d][e]:
                continue
        if not condition2_list:
            u = condition1_list[0][0]
            v = condition1_list[0][1]
            condition2_list.append((u, v))
        f = condition2_list.pop()
        classroom[f[0]][f[1]] = student
    else:
        h = condition1_list.pop()
        classroom[h[0]][h[1]] = student

satisfy = 0
result = 0
for n in range(N):
    for m in range(N):
        satisfy = 0
        for z in range(len(info)):
            if classroom[n][m] == info[z][0]:
                for o in range(4):
                    ox = dx[o] + n
                    oy = dy[o] + m
                    if ox < 0 or ox >= N or oy < 0 or oy >= N:
                        continue
                    if classroom[ox][oy] == info[z][1]:
                        satisfy += 1
                    if classroom[ox][oy] == info[z][2]:
                        satisfy += 1
                    if classroom[ox][oy] == info[z][3]:
                        satisfy += 1
                    if classroom[ox][oy] == info[z][4]:
                        satisfy += 1
                if satisfy == 0:
                    result += 0
                elif satisfy == 1:
                    result += 1
                elif satisfy == 2:
                    result += 10
                elif satisfy == 3:
                    result += 100
                elif satisfy == 4:
                    result += 1000
print(result)


