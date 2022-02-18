arr = [[2,1,8,3,5], [7,3,1,9,4], [4,2,5,1,3], [1,4,1,6,9], [3,2,8,7,1]]

T = int(input())

def part_down(r,c):
    tmp = arr[r+2][c]
    for i in range(2,0,-1):
        arr[r+i][c] = arr[r+i-1][c]
    arr[r][c] = tmp

for tc in range(T):
    x, y = map(int,input().split())
    part_down(x,y)

for i in range(5):
    print(*arr[i])
