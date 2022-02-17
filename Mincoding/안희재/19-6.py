map = [[3,3,5,3,1], [2,2,4,2,6], [4,9,2,3,4], [1,1,1,1,1], [3,3,5,9,2]]

dx = [-1,-1,1,1] # 11시 시작, 시계방향 , x는 행
dy = [-1,1,-1,1] # y는 열

def sum(x,y):
    sum1 = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
            sum1 += map[nx][ny]
    return sum1

max = 0
max_position = (0,0)
for i in range(5):
    for j in range(5):
        if sum(i,j) > max:
            max = sum(i,j)
            max_position = (i,j)

print(*max_position)