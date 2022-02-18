arr = [[1,4,9,0,2], [8,5,6,7,7], [7,2,3,2,1], [7,1,4,3,8], [9,4,0,5,7]]
T = int(input())

def row_move(a,b): # a,b는 좌표
    tmp = arr[a][b+2]
    for i in range(2,0,-1):
        arr[a][b+i] = arr[a][b+i-1]
    arr[a][b] = tmp

def col_move(a,b):
    tmp = arr[a+2][b]
    for i in range(2,0,-1):
        arr[a+i][b] = arr[a+i-1][b]
    arr[a][b] = tmp

for tc in range(T):
    x, y, direct = map(int,input().split()) 
    if direct: # direct가 1이면 세로 이동
        col_move(x,y)
    else:
        row_move(x,y)

for i in range(5):
    print(*arr[i])
