import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
Max, Min = -1000000001, 1000000001

# idx로 숫자 입력 받은거 차례로
def dfs(idx, answer, add, sub, mul, div):
    global Max, Min
    if idx == N:
        Max = max(Max, answer)
        Min = min(Min, answer)
        return
    # answer에 값 누적하고 쓴 연산자 한개씩 빼주기
    if add:
        dfs(idx + 1, answer + arr[idx], add - 1, sub, mul, div)
    if sub:
        dfs(idx + 1, answer - arr[idx], add, sub - 1, mul, div)
    if mul:
        dfs(idx + 1, answer * arr[idx], add, sub, mul - 1, div)
    if div:
        if answer < 0:
            dfs(idx + 1, -(-answer // arr[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, answer // arr[idx], add, sub, mul, div - 1)


dfs(1, arr[0], operator[0], operator[1], operator[2], operator[3])
print(Max)
print(Min)