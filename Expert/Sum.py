for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    vertical, horizontal, right, left = 0, 0, 0, 0
    Max = 0
    for i in range(100):
        vertical, horizontal = 0, 0
        for j in range(100):
            vertical += arr[i][j]
            horizontal += arr[j][i]
            if i == j:
                left += arr[i][j]
            if j == 99-i:
                right += arr[i][j]
        Max = max(Max, vertical, horizontal)
    Max = max(Max, left, right)
    print("#{} {}".format(t, Max))