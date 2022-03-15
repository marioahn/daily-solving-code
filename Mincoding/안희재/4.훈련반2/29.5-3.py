arr = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    tmp = arr[i][0]
    if sum(arr[i]) == tmp * 3:
        print(tmp)
    else:
        print('x')