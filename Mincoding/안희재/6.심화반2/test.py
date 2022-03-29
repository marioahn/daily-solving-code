from collections import deque

N = int(input()) # N * N
arr = [list(input()) for _ in range(N)]
sx, sy = map(int,input().split())
position = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            position.append((i,j))

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
for i in range(2,3):
    cnt = 0
    tx, ty = position[i][0], position[i][1]
    visit2 = [[0] * N for _ in range(N)]
    bfsF(tx,ty,0) # 소화기에서 불까지
    if Min > cnt:
        Min = cnt

print(Min)
