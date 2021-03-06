'''
예시정렬 1.
[3, 30, 32, 34]
정답 34→ 3→ 32→ 30
3은 한자리 숫자 이지만 , 나머지 두자리 숫자의
두번째 숫자(32의 경우 2 /30의 경우 0/ 34 의 경우 4 ) 와 3을 비교하여 두번째수가 크면 우선순위에 , 작으면 3보다 이전 숫자가 됨  4>3>2>0

예시정렬 2.
[53, 534, 531]
534  와 531 의경우는 자릿수가 같기때문에 자릿수를 검사하면서
큰 수 뽑기 → 53까지는 같고 4가 1보다 크니까 534 가 우선
자릿수가 다른 53과 534, 53과 531은
세번째 수를 첫째자리인 5와 비교하기
5>4>1 이기 때문에 53이 제일 우선순위를 가짐

모든 수의 범위가 1000 이하이므로
최소한의 자릿수인 한자리수가 셋째자리 숫자를 가질 수 있도록 x3을 한 후,
큰 것 부터 앞으로 (내림차순 정렬)
'''


def solution(numbers):
    answer = ''
    # numbers 를 string으로
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    for i in numbers:
        answer += i
    # [0,0,0,0]의 경우 0000 이 나오므로 정수형으로 변환 후 다시 string으로 바꾸기
    answer = str(int(answer))
    return answer

def solution(numbers):
    answer = ''
    if numbers.count(0)==len(numbers):
        return "0"
    for i in range(0,len(numbers)):
        numbers[i]=str(numbers[i])
    numbers.sort(reverse=True)
    i=1
    while i<=len(numbers)-1:
        if numbers[i]+numbers[i-1] > numbers[i-1]+numbers[i]:
            a=numbers[i-1]
            numbers[i-1]=numbers[i]
            numbers[i]=a
            i-=2
        i+=1
    for i in range(0,len(numbers)):
        answer+=numbers[i]
    return answer