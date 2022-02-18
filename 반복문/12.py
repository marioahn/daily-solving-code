arr = [[1,3,5,2], [2,4,9,3], [7,2,0,1], [5,8,2,4]]
N = int(input())

def step1(array, num):
    for i in range(num):
        tmp = arr[0][3]
        for j in range(3,0,-1): # 3,2,1
            arr[0][j] = arr[0][j-1]
        arr[0][0] = tmp

def step2(array, num):
    for i in range(num):
        tmp = arr[3][3]
        for j in range(3,0,-1):
            arr[j][3] = arr[j-1][3]
        arr[0][3] = tmp

def step3(array, num):
    for i in range(num):
        tmp = arr[3][0]
        for j in range(0,3):
            arr[3][j] = arr[3][j+1]
        arr[3][3] = tmp

def step4(array, num):
    for i in range(num):
        tmp = arr[0][0]
        for j in range(0,3):
            arr[j][0] = arr[j+1][0]
        arr[3][0] = tmp

step1(arr,N)
step2(arr,N)
step3(arr,N)
step4(arr,N)

for i in range(4):
    print(*arr[i])