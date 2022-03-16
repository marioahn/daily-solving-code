x, y = map(int,input().split()) # x는 행, y는 열
arr = [list(map(int,input().split())) for _ in range(x)]

for i in range(3):
    max = 0
    a, b = 0, 0
    for i in range(x):
        for j in range(y):
            if arr[i][j] > max:
                max = arr[i][j]
                a, b = i, j

    arr[a][b] = 0
    print(f'{max}({a},{b})')