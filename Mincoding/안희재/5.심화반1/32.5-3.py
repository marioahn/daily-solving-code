arr = [
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S']]

word = input()
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

for k in range(len(word)):
    x, y = 0, 0
    flag = 0
    for i in range(3):
        for j in range(6):
            if word[k] == arr[i][j][0]: # [0] 추가해줘야.. 'HAA'인 경우, A는 'A#'상태라서;;
                x, y = i, j
                flag = 1
                break
        if flag:
            break
    if len(arr[x][y]) == 1: # 'A#' 상태라서; 이 코드 추가 안해주면 A#### 가 출력됨;
        arr[x][y] += '#'
    else:
        arr[x][y] = arr[x][y][0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < 3 and 0 <= ny < 6:
            if len(arr[nx][ny]) == 1:
                arr[nx][ny] += '#'
            elif len(arr[nx][ny]) == 2: # 'C#' 이런상태니까, ㅎㅎ굳이 tmp로 뒤집기전 알파벳 저장안해도 됨!
                arr[nx][ny] = arr[nx][ny][0] # 여기 if로 하면 안되잖아..ㅋㅋㅋ위에서 1추가하고, 바로 여기서 다시 빠짐.. 무슨의미냐!!

for i in range(3):
    for j in range(6):
        if len(arr[i][j]) == 2:
            arr[i][j] = arr[i][j][1]

for i in range(3):
    print(*arr[i],sep='')

# 'HAA'