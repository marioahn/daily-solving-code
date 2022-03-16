angle = int(input())

arr = [12,3,6,9] # 12 3 6 9시

def move():
    tmp = arr[-1]
    for i in range(3,0,-1):
        arr[i] = arr[i-1]
    arr[0] = tmp

for i in range(angle//90):
    move()

def move2(): # 출력은 12시,3시,9시,6시순으로 나와야함
    tmp = arr[-1]
    for i in range(3,1,-1):
        arr[i] = arr[i-1]
    arr[1] = tmp

move2()
print(*arr)