n = int(input()) # 회전 횟수
rotation = list(map(int,input().split()))

arr = [[1,5,9], [7,0,3], [4,2,8]]

# 가로회전, 세로회전함수 따로 만들어야 할듯?
# 0~2면 가로회전, 3~5면 세로회전

def r_move(num):
    tmp = arr[num][2]
    for i in range(2,0,-1):
        arr[num][i] = arr[num][i-1]
    arr[num][0] = tmp

def c_move(num): # 세로 이동 함수 짜는게 은근 귀찮았네..
    tmp = arr[2][num-3]
    for i in range(2,0,-1): # i는 2,1
        arr[i][num-3] = arr[i-1][num-3]
    arr[0][num-3] = tmp

for i in rotation:
    if i <= 2:
        r_move(i)
    else:
        c_move(i)

for i in range(3):
    print(*arr[i])
