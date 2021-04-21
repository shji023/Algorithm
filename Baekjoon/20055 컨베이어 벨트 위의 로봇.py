import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
con = deque(map(int, input().split()))
robot = deque([0]*n)
result = 0

while True:
    # 1 벨트회전하면 로봇도 같이 화전
    con.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2, -1, -1):
            # 2 가장 먼저 벨트에 올라간 로봇부터, 다음칸 로봇이 없으며 내구도가 1이상
            if robot[i] == 1 and robot[i+1] == 0 and con[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                con[i+1] -= 1
        robot[-1] = 0
    # 3 올라가는 위치에 로봇이 없으면 올리기
    if robot[0] == 0 and con[0] >= 1:
        robot[0] = 1
        con[0] -= 1
    result += 1
    # 4
    if con.count(0) >= k:
        break
print(result)