arr = [list(map(str,input())) for _ in range(4)]
monster = ['']*3
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            monster[0] = [i,j]
        elif arr[i][j] == 'C':
            monster[1] = [i,j]
        elif arr[i][j] == 'D':
            monster[2] = [i,j]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
second = 0
while second < 5:
    for i in range(3):
        idx = second % 4
        y,x = monster[i]
        if 0 <= x+dx[idx]<= 2 and 0 <= y+dy[idx]<= 2 and arr[y+dy[idx]][x+dx[idx]] =='_':
            arr[y][x], arr[y+dy[idx]][x+dx[idx]] = arr[y+dy[idx]][x+dx[idx]], arr[y][x]
            monster[i] = y+dy[idx], x+dx[idx]
    second += 1
for i in range(4):
    print(*arr[i],sep='')