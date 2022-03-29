arr = [list(input()) for _ in range(4)]

def rotate(x,y): # x,y를 중심으로 테두리 회전(3*3배열)
    arr1 = [[x+1,y-1],[x,y-1],[x-1,y-1], [x+1,y],[x,y],[x-1,y], [x+1,y+1],[x,y+1],[x-1,y+1]] # rotate

    arr2 = [[0] * 3 for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            arr2[i][j] = arr[arr1[k][0]][arr1[k][1]] 
            k += 1

    a = 0
    for i in range(x-1,x+2):
        b = 0
        for j in range(y-1,y+2):
            arr[i][j] = arr2[a][b]
            b += 1
        a += 1

rotate(1,2)
rotate(2,1)
rotate(1,2)


for i in range(4):
    print(*arr[i],sep='')