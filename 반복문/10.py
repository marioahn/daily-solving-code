arr = [[1,3,5], [2,4,9], [7,2,0], [5,8,2]]

n = int(input())

def r_move(array):
    for i in range(4):
        tmp = arr[i][2]
        for j in range(2,0,-1):
            arr[i][j] = arr[i][j-1]
        arr[i][0] = tmp

def l_move(array):
    for i in range(4):
        tmp = arr[i][0]
        for j in range(0,2):
            arr[i][j] = arr[i][j+1]
        arr[i][2] = tmp

if n > 0:
    for i in range(n):
        r_move(arr)
else:
    for i in range(n * -1):
        l_move(arr)

for i in range(4):
    print(*arr[i])
