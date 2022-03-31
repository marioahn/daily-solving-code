# 도착지점에서 거꾸로 올라가는 DP 구현
# (0,0)시작 / (3,3)도착
arr = [list(map(int,input().split())) for _ in range(4)]
accu = [[0] * 4 for _ in range(4)] # 누적합 담을 함수
way = [[0] * 4 for _ in range(4)]

def sett():
    for i in range(2,-1,-1):
        accu[3][i] = accu[3][i+1]+arr[3][i]
        accu[i][3] = accu[i+1][3]+arr[i][3]
        way[3][i] = 'right'
        way[i][3] = 'down'

sett() # 초기값들 세팅하고, 이제 아래에서 업데이트 예정
for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        down = accu[i+1][j]
        right = accu[i][j+1]

        if down > right:
            accu[i][j] = arr[i][j] + right
            way[i][j] = 'right'
        else:
            accu[i][j] = arr[i][j] + down
            way[i][j] = 'down'

x,y = 0,0
while 1:
    if x == 3 and y == 3:
        print('3,3')
        break
    print(f'{x},{y}')
    if way[x][y] == 'down':
        x += 1
    else:
        y += 1



