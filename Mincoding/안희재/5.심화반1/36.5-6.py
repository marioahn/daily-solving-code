n, k = map(int,input().split()) # n*n 사이즈
arr = [input().split() for _ in range(n)]

for i in range(k):
    x, y, z = map(int,input().split()) # x,y는 좌표 / z는 집게타입
    if z == 1:
        result = ''
        dx = [-1,0,0,0,1]
        dy = [0,0,-1,1,0]
        for j in range(5):
            if 0 <= x+dx[j] < n and 0 <= y+dy[j] < n:
                print(arr[x+dx[j]][y+dy[j]], end='')
        print()

    if z == 2:
        dx = [-1,0,-1,1,1]
        dy = [-1,0,1,1,-1]
        for j in range(5):
            if 0 <= x+dx[j] < n and 0 <= y+dy[j] < n:
                print(arr[x+dx[j]][y+dy[j]], end='')
        print()
