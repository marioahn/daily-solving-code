# 제자리 점프까지 구현한 코드
from collections import deque
arr = [[0,0,0,'X',0], [0,0,0,'X',0], ['X','X',0,0,0], [0,0,'X',0,0], [0,0,0,0,0]] # 'X'는 빙판
lx, ly = map(int,input().split()) # 엘사
ax, ay = map(int,input().split()) # 안나

def bfs_A(x,y,level):
    q = deque()
    q.append((x,y,level))

    while q:
        nowx,nowy,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<5 and 0<=dy<5): continue
            if arr[dx][dy] == 'X': continue
            if arr[dx][dy] == 0:
                arr[dx][dy] = level+1 # +1씩!
                q.append((dx,dy,level+1))
            
arr[ax][ay] = 1 
bfs_A(ax,ay,1) 

def bfs_L(x,y,level):
    q = deque()
    q.append((x,y,level))

    while q:
        nowx,nowy,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<5 and 0<=dy<5): continue
            if arr[dx][dy] == 'X': continue
            if arr[dx][dy] * (-1) == level-1: # 딱 만나는 경우
                return (-1) * (level)
            if abs(arr[dx][dy]+(level-1)) <= 1: # 제자리 점프 -> 이렇게만 하면 됨!
                return (-1) * (level-1) # 대신, 여기는 level-1로 줘야하고!
            if arr[dx][dy] > 0:
                arr[dx][dy] = level-1 # -1씩!
                q.append((dx,dy,level-1))

arr[lx][ly] = -1
print(bfs_L(lx,ly,-1))

# 3 1
# 1 4