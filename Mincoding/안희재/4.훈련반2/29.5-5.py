arr = []
for i in range(4):
    arr.append(list(map(int,input().split())))

# ..? 왼쪽으로 향하는 블록인 경우도 따로해야하나? 머지 이 문제..?
# 첫 1 포착

x, y, flag = 0, 0, 0
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            x, y = i, j
            flag = 1
            break
    if flag:
        break
x1, y1 = x, y

while 1:
    x += 1
    if arr[x][y] == 0:
        x -= 1
        break

if arr[x][y-1] == 0: # 우측 블록
    while 1:
        y += 1
        if y == 5:
            y-= 1
            break
        if arr[x][y] == 0:
            y -= 1
            break
else: # 좌측으로 가는 블록
    while 1:
        y -= 1
        if y == -1:
            y += 1
            break
        if arr[x][y] == 0:
            y += 1
            break

x2, y2 = x, y

print(f'({x1},{y1})')
print(f'({x2},{y2})')