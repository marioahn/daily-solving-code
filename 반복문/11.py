arr = [[2,5,4], [6,3,7], [8,9,9], [3,2,1]]
N = int(input())

def down(array):
    for i in range(3): # 3 = 열의 길이
        tmp = arr[3][i]
        for j in range(3,0,-1):
            arr[j][i] = arr[j-1][i]
        arr[0][i] = tmp

def up(array):
    for i in range(3):
        tmp = arr[0][i]
        for j in range(0,3):
            arr[j][i] = arr[j+1][i]
        arr[3][i] = tmp

if N > 0:
    for i in range(N):
        down(arr)
else:
    for i in range(-N):
        up(arr)

for i in range(4):
    print(*arr[i])