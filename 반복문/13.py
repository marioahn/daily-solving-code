arr = [[2,'#',3], ['#',4,'#'], [8,'#',5]]

way, n = input().split()
n = int(n)

def R_move(array, num):
    for i in range(num):
        tmp = arr[2][2]
        for j in range(2,0,-1):
            arr[j][j] = arr[j-1][j-1]
        arr[0][0] = tmp

def L_move(array, num):
    for i in range(num):
        tmp = arr[2][0]
        for j in range(2,0,-1):
            arr[j][2-j] = arr[j-1][2-j+1]
        arr[0][2] = tmp

if way == 'R':
    R_move(arr,n)
else:
    L_move(arr,n)

for i in range(3):
    print(*arr[i])