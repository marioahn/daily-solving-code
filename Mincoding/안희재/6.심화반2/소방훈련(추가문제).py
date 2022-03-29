# '#'벽 / A 소화기 / $ 불 / _ 빈공간
# 1. 소화기 위치 좌표 입력받고,
# 2. 각각 bfs돌려서 최소 이동횟수 print
# 성공..................! 힘들었다........
from collections import deque

N = int(input()) # N * N
arr = [list(input()) for _ in range(N)]
sx, sy = map(int,input().split())
position = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            position.append((i,j))

def bfsA(x,y,level): # 현재위치에서 A(소화기)로 가는 bfs
    global cnt, tx, ty
    q = deque()
    q.append((x,y,level))

    while q:
        nowx, nowy, level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]
        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<N and 0<=dy<N): continue
            if arr[dx][dy] == '#' or arr[dx][dy] == '$' or visit[dx][dy] == 1: continue # 아.. 불도 못가지..
            if dx == tx and dy == ty:
                cnt += level+1
                return
            arr[dx][dy], visit[dx][dy] = level+1, 1
            q.append((dx,dy,level+1))
            
def bfsF(x,y,level): # 현재위치(소화기)에서 F(불)로 가는 bfs
    global cnt
    q = deque()
    q.append((x,y,level))

    while q:
        nowx,nowy,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]
        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<N and 0<=dy<N): continue
            if arr[dx][dy] == '#' or visit2[dx][dy] == 1: continue
            if arr[dx][dy] == '$':
                cnt += level+1
                return
            arr[dx][dy], visit2[dx][dy] = level+1, 1
            q.append((dx,dy,level+1))

Min = 2e18
for i in range(len(position)):
    cnt = 0
    tx, ty = position[i][0], position[i][1]
    visit = [[0] * N for _ in range(N)]
    bfsA(sx,sy,0) # -> sx,sy위치는 소화기위치로 바뀌게 됨
    visit2 = [[0] * N for _ in range(N)]
    bfsF(tx,ty,0) # 소화기에서 불까지
    if Min > cnt:
        Min = cnt

print(Min)

