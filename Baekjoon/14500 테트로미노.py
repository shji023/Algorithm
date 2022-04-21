import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
shape = [
    # ㅡ
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # ㅁ
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # ㄴ
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 1], [1, 1], [2, 0], [2, 1]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    # ㄹ
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [0, 2], [1, 0], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # ㅗ
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 0]],
]

for i in range(N):
    for j in range(M):
        for s in shape:
            result = 0
            for k in range(4):
                try:
                    result += arr[i+s[k][0]][j+s[k][1]]
                except IndexError:
                    continue
            answer = max(result, answer)

print(answer)

# 스스로 풀기
import sys

sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
# 1,2,8,6,3,5,4
dx = [[0,0,0],[1,1,1],
      [0,1,0],
      [1,1,0],[1,1,0],[1,0,0],[0,1,1],[0,0,1],[0,1,1],[0,0,1],[1,0,0],
      [1,0,1],[1,0,1],[0,1,0],[0,1,0],
      [0,0,1],[1,0,1],[1,1,-1],[1,0,0]
      ]
dy = [[1,1,1],[0,0,0],
      [1,0,-1],
      [0,0,1],[0,0,-1],[0,-1,-1],[1,0,0],[1,1,-2],[1,-1,0],[1,1,0],[0,1,1],
      [0,1,0],[0,-1,0],[1,-1,-1],[1,0,1],
      [1,1,-1],[0,1,-1],[0,0,-1],[-1,1,1]
      ]
Max = 0
for x in range(N):
    for y in range(M):
        for k in range(len(dx)):
            nx, ny = x, y
            cnt = arr[x][y]
            for t in range(3):
                nx = dx[k][t]+nx
                ny = dy[k][t]+ny
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                cnt += arr[nx][ny]
            else:
                Max = max(Max, cnt)
print(Max)
