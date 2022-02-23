arr = [[9,1,0,7], [3,2,6,1], [4,0,8,2], [5,9,2,3]]
N = int(input())
# 가운데는 시계방향으로
# 바깥 테두리는 반시계방향으로

def move():
    # step0 - 가운데
    stmp1 = arr[1][1]
    stmp2 = arr[1][2]
    stmp3 = arr[2][2]
    stmp4 = arr[2][1]

    arr[1][2] = stmp1
    arr[2][2] = stmp2
    arr[2][1] = stmp3
    arr[1][1] = stmp4

    tmp1 = arr[3][0]
    tmp2 = arr[3][3]
    tmp3 = arr[0][3]

    # step1
    for i in range(3,0,-1):
        arr[i][0] = arr[i-1][0]
    # step2
    for i in range(3,0,-1):
        arr[3][i] = arr[3][i-1]
    # step3
    for i in range(0,3):
        arr[i][3] = arr[i+1][3]
    # step4
    for i in range(0,3):
        arr[0][i] = arr[0][i+1]

    arr[3][1] = tmp1
    arr[2][3] = tmp2
    arr[0][2] = tmp3

for i in range(N):
    move()

for i in range(4):
    print(*arr[i])