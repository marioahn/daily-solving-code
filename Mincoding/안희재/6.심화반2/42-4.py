from collections import deque
arr = [list(input()) for _ in range(3)]
# 음.. bfs4번해야하나?
# visit만들고, 각각 초기화시키면 될듯?

def bfs(x,y,level):
    global cnt, sx, sy, tmp
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
            if arr[dx][dy] == '#' or visit[dx][dy] == -1:continue
            if arr[dx][dy] == str(target):
                level += 1
                tmp = level
                sx, sy = dx, dy
                return
            visit[dx][dy] = -1 # 방문흔적
            q.append((dx,dy,level+1))

sx,sy = 0,0 #startx,starty
Sum, tmp = 0, 0
for target in range(1,5):
    visit = [[0]*5 for _ in range(3)]
    visit[sx][sy] = -1
    bfs(sx,sy,0)
    Sum += tmp

print(f'{Sum}회')