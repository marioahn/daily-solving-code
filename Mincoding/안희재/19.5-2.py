from unittest.result import failfast


arr = []
for i in range(5):
    arr.append(list(map(int,input().split())))

# direct쓰는건가?
dx = [-1,-1,-1,0,0,1,1,1] # 11시부터 1렬 쭈욱, 그 다음 행 1렬 쭈욱 ...
dy = [-1,0,1,-1,1,-1,0,1]

def check(x,y):
    status = ''
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0<= ny < 4:
            if arr[nx][ny] == 1:
                status = 'bad'
            else:
                status = 'good'
    return status

for i in range(5):
    result = '안정된 상태'
    break_point = True
    break_point2 = True
    for j in range(4):
        if arr[i][j] == 1:
            if check(i,j) == 'bad':
                result = '불안정한 상태'
                break_point = False
                break
            else:
                continue
        if break_point == False:
            break_point2 = False
            break
    if break_point2 == False:
        break

print(result)



# 아 또 이러네.. 이중반복문 break빠져나오는 법. 굳이 이렇게까지 해야되나 어떻게 했었지