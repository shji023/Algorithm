# 회문 문자열 검사 *
N = int(input())
for t in range(N):
    cnt = 0
    temp = input()
    a = temp.lower()
    x = len(a)
    for i in range(x//2):
        if a[i] == a[x-1-i]:
            continue
        else:
            cnt += 1
    if cnt == 0:
        print("#%d" %(t+1), "YES")
    else:
        print("#%d" % (t+1), "NO")

'''
인덱스 거꾸로 접근
s[-1]
s[::-1]
s 문자열 거꾸로 바꿈
'''

# 숫자만 추출 *
a = input()
number = ""
cnt = 0
for x in a:
    if x.isdecimal():
        number += x
for i in range(1, int(number)+1):
    if int(number)%i == 0:
        cnt += 1
print(int(number))
print(cnt)
'''
res = 0
res = res *10 int(x)
'''

# 카드 역배치(정올 기출) *
array = list(range(1, 21))

for x in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        temp = array[a-1 + i]
        array[a-1 + i] = array[b-1 - i]
        array[b-1 - i] = temp
for x in array:
    print(x, end=' ')
'''
python swap
a, b = b, a
그냥 반복할 경우(변수 대입하는 것도 시간이 걸리니까)
for _ in range(10):
제일 앞에것 꺼내기
a.pop(0)
'''

# 두 리스트 합치기 *
N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

array = a + b

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
for x in array:
    print(x, end=' ')

# 수의 합
'''
이중 포문으로 타임에러가 나는 코드 *
'''
N, M = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)):
    sum = a[i]
    for j in range(i+1, len(a)):
        if sum != M:
            sum += a[j]
        if sum == M:
            cnt += 1
            break
print(cnt)

'''
해설 코드
N, M = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
lt = 0
rt = 1
tot = a[0]
while True:
    if tot < M:
        if rt < N:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == M:
        cnt +=1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
'''

# 격자판 최대합 *
N = int(input())
array = []
max = -2147000000
rowSum = colSum = diaSum = diaSum2 = 0
for _ in range(N):
    a = list(map(int, input().split()))
    array.append(a)
for i in range(len(array)):
    rowSum = colSum = 0
    for j in range(len(array)):
        rowSum += array[i][j]
        colSum += array[j][i]
        if i == j:
            diaSum += array[i][j]
    diaSum2 += array[i][len(array)-1-i]
    if rowSum > max:
        max = rowSum
    if colSum > max:
        max = colSum
    if diaSum > max:
        max = diaSum
    if diaSum2 > max:
        max = diaSum2
print(max)
'''
a = [list(map(int, input().split())) for _ in range(N)]
'''

# 사과나무 *
N = int(input())
array = []
sum = 0
start = end = N//2
for _ in range(N):
    a = list(map(int, input().split()))
    array.append(a)
size = len(array)
for i in range(size):
    for j in range(start, end + 1):
        sum += array[i][j]
    if i < N//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
print(sum)

# 곶감(모래시계) - 답안참조
N = int(input())
array = []
sum = 0
start = end = N//2
for _ in range(N):
    a = list(map(int, input().split()))
    array.append(a)

M = int(input())
for _ in range(M):
    b = list(map(int, input().split()))
    for _ in range(b[2]):
        if b[1] == 0:
            array[b[0]-1].append(array[b[0]-1].pop(0))
        else:
            array[b[0] - 1].insert(0, array[b[0] - 1].pop())

start = 0
end = N-1
size = len(array)
for i in range(size):
    for j in range(start, end + 1):
        sum += array[i][j]
    if i < N//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(sum)
'''
a[n].append(a[n].pop(0))
제일 앞에있는 자료를 빼내고 다 앞으로 한칸씩 땡김 그리고 그 자료를 append

a[n].insert(a[n].pop())
제일 뒤에 있는 자료 꺼내 맨앞으로 넣기 - insert
'''

# 봉우리 *
import sys
sys.stdin = open("input.txt", 'r')
'''
# feedback
# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
'''
n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
a. insert(0, [0]*n)
a. append([0]*n)
answer = 0
for x in a:
    x.insert(0, 0)
    x.append(0)
for i in range(1, n+1):
    for j in range(1, n+1):
        now = a[i][j]
        up = a[i-1][j]
        down = a[i+1][j]
        left = a[i][j-1]
        right = a[i][j+1]
        # if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
        if now > up and now > down and now > left and now > right:
            answer += 1

print(answer)

# 스도쿠 검사 - 답안 참조
def check(a):
    for i in range(9):
        # 행을 체크하기 위한 배열
        row_ch = [0]*10
        # 열을 체크하기 위한 배열
        col_ch = [0]*10
        for j in range(9):
            row_ch[a[i][j]] = 1
            col_ch[a[j][i]] = 1
        if sum(row_ch) != 9 or sum(col_ch) != 9:
            return False
    for i in range(3):
        for j in range(3):
            # 3 * 3 그룹을 체크하기 위한 배열
            group_ch = [0]*10
            for k in range(3):
                for s in range(3):
                    group_ch[a[i*3+k][i*3+s]] = 1
            if sum(group_ch) != 9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")

# 격자판 회문수 *
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        if a[i][j] == a[i][j+4] and a[i][j+1] == a[i][j+3]:
            cnt += 1
for y in range(7):
    for x in range(3):
        if a[x][y] == a[x+4][y] and a[x+1][y] == a[x+3][y]:
            cnt += 1
print(cnt)
'''
# 0~4 열 까지 슬라이스 (가로)
tmp = a[j][i:i+5]
# 회문체크(역순과 같은지)
if tmp == tmp[::-1]
'''