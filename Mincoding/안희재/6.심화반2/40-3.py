# DP로
# 0은 벽, 방향은 왼아래,아래,오른아래
# 7*3맵 / 시작은 (0,0) / 끝은 맨 아래행으로 내려왔을때 : 즉 i == 6

# 난 거꾸로 올라갈 것임
arr = [list(map(int,input().split())) for _ in range(7)]
accu = [[0] * 3 for _ in range(7)]

def sett():
    for i in range(3):
        accu[6][i] = arr[6][i] # 이건 그대로

sett() # 실행

for i in range(5,-1,-1):
    for j in range(2,-1,-1): # 왼아,아래,오아이기 때문에 여기는 그냥 2임(1부터가 x)
        if arr[i][j] == 0: continue # 벽이면 아예 pass시켜줘야 함
        if i+1<=6 and j-1>=0:
            leftd = accu[i+1][j-1]
        else:
            leftd = 0
        if i+1<=6:
            down = accu[i+1][j]
        else:
            down = 0
        if i+1<=6 and j+1<=2:
            rightd = accu[i+1][j+1]
        else:
            rightd = 0

        accu[i][j] = max(leftd,down,rightd)+arr[i][j]
        
print(accu[0][0])
