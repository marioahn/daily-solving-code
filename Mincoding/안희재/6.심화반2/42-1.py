from collections import deque
arr = [[0,0,0,0], [1,1,0,1], [0,0,0,0], [1,0,1,0]]
sx,sy = map(int,input().split())
ex,ey = map(int,input().split())


def bfs(x,y,level):
    q = deque()
    q.append((x,y,level))

    while q:
        nowx,nowy,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<4 and 0<=dy<4): continue
            if arr[dx][dy] > 0: continue
            if dx == ex and dy == ey: # 모든 스택비울때까지 갈 필요 없음!
                return level
            arr[dx][dy] = level+1
            q.append((dx,dy,level+1))


arr[sx][sy] = 1
print(f'{bfs(sx,sy,1)}회')
