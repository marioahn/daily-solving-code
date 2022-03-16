a = [list(map(int,input().split())) for _ in range(3)]
input()
b = [list(map(int,input().split())) for _ in range(3)]


cnt = 0
while 1:
    x = [[0] * 3 for _ in range(3)]
    if a == b:
        print(cnt)
        break
    for i in range(3):
        for j in range(3):
            x[j][i] = a[i][2-j]
    cnt += 1
    a = x