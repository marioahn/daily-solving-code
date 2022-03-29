# 아. 아래 코드는 visit배열이 없음..
# 일단 target 찾으면 바로 리턴이라 큰 문제는 없음 ㅇㅇ;;
# 만약,target찾는 문제가 아니라 그냥 꽉 채우는 문제였으면 무한재귀..
from collections import deque
arr = [[0,0,0,0,1], [1,0,1,0,0], [0,0,0,0,1]]
travel = []
for i in range(2):
    x, y = map(int,input().split()) # cheese, 친구위치
    travel.append((x,y))

def bfs(x,y,level):
    global sx, sy, tx,ty, cnt
    q = deque()
    q.append((x,y,level))

    while q:
        nowx,nowy,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<3 and 0<=dy<5): continue
            if arr[dx][dy] == 1: continue
            if dx == tx and dy == ty:
                sx, sy = dx, dy
                level += 1
                cnt = level
                return
            arr[dx][dy] = -1
            q.append((dx,dy,level+1))

Sum = 0         
sx, sy = 0, 0 # 초기위치(start)
for i in range(2):
    cnt = 0
    tx, ty = travel[i][0], travel[i][1] # target_x,target_y
    bfs(sx,sy,0)
    Sum += cnt

print(Sum)
# 음;; 근데 sx,sy,tx,ty,level,cnt까지. 이렇게 변수 여러개 만들 문제인가.....?
# 아닌것 같은데 뭐지;;
