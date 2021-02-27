N = int(input())
dic = {}
max_arr = []

for i in range(N):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
# 최대 value 값 찾기
max_value = max(dic.values())
# 딕셔너리 객체화
for x in dic.items():
    if x[1] == max_value:
        max_arr.append(x[0])
# 정렬 후 사전 순 가장 앞에있는 값 출력
sorted_arr = sorted(max_arr)
print(sorted_arr[0])