from collections import deque
arr = [list(map(int,input().split())) for _ in range(4)]
# 출발점은 0,0

cnt = 0
def bfs(x,y):
    global cnt
    q = deque()
    q.append((x,y))

    while q:
        nowx,nowy = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<4 and 0<=dy<6): continue
            if arr[dx][dy] == 1 or arr[dx][dy] == -1: continue
            if arr[dx][dy] == 2: cnt += 1 # 고기 get
            arr[dx][dy] = -1 # 지나간 흔적
            q.append((dx,dy))

arr[0][0] = -1
bfs(0,0)
print(cnt)


