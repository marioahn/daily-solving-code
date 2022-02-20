arr = [[1,0,7,2], [5,3,0,6], [6,9,2,3], [3,5,6,2]]

N = int(input())

def move(x,y):
    tmp1 = arr[x][y] # 11시
    tmp2 = arr[x][y+1] # 1시
    tmp3 = arr[x+1][y+1] # 5시
    tmp4 = arr[x+1][y] # 7시
    arr[x][y] = tmp4
    arr[x][y+1] = tmp1
    arr[x+1][y+1] = tmp2
    arr[x+1][y] = tmp3

for i in range(0,3,2): # 0, 2
    for j in range(0,3,2): # 0, 2
        move(i,j)

print(arr)

# 케이스 자체가 간단한데, 만약 4*4가 아니라, 가변적인 크기였다면?
# -> 코드 더 짜서 넣어야 함