arr = [[1,2,3], [4,5,6], [7,8,9]]
N = int(input())



def move():
    tmp1 = arr[0][2]
    tmp2 = arr[2][2]
    tmp3 = arr[2][0]
    # step1 - 윗줄 이동
    for i in range(2,0,-1):
        arr[0][i] = arr[0][i-1]

    # step2 - 오른쪽을 이동
    for i in range(2,0,-1):
        arr[i][2] = arr[i-1][2]

    # step3 - 아랫줄 이동
    for i in range(0,2):
        arr[2][i] = arr[2][i+1]

    # step4 - 왼쪽줄 이동
    for i in range(0,2):
        arr[i][0] = arr[i+1][0]

    arr[1][2] = tmp1
    arr[2][1] = tmp2
    arr[1][0] = tmp3

for i in range(N):
    move()

for i in range(3):
    print(*arr[i])