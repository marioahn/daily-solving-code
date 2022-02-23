arr =[[3,1,5,7,9], [2,7,8,1,3], [6,8,2,1,0], [1,0,4,8,2], [9,8,2,1,4]]

N = int(input())

def move():
    tmp1 = arr[0][4]
    tmp2 = arr[4][4]
    tmp3 = arr[4][0]
    # step1
    for i in range(4,0,-1):
        arr[0][i] = arr[0][i-1]
    # step2
    for i in range(4,0,-1):
        arr[i][4] = arr[i-1][4]
    # step3
    for i in range(0,4):
        arr[4][i] = arr[4][i+1]
    # step4
    for i in range(0,4):
        arr[i][0] = arr[i+1][0]

    arr[1][4] = tmp1
    arr[4][3] = tmp2
    arr[3][0] = tmp3

move()

for i in range(5):
    print(*arr[i])