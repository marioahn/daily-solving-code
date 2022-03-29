from collections import deque
# 제자리..? 일단 이건 패스하고 구현해보자
# bfs2개 만들고, 안나는 +1, 엘사는 -1로 퍼지도록
    # 안나꺼 먼저 floodfill 돌림
    # 그러면, 맵이 +1씩 퍼져있는 상태 -> 엘사꺼 -1씩하는데, 
    # 중간에 -1를 곱한 level이 맵의 상태와 같으면 리턴하고 cnt세기
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
            
arr[ax][ay] = 1 # 자기자신 1, level은 1부터 시작 -> 처음 전파시 2로!
bfs_A(ax,ay,1) # 안나의 영향력으로 맵이 채워진 상태 (전부 양수 or 'X')

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
            if arr[dx][dy] * (-1) == level-1: # 만나는 지점!
                return (-1) * (level) # 시작이 1이니까 음수에서 1+ 해줘야함
            if arr[dx][dy] > 0:
                arr[dx][dy] = level-1 # -1씩!
                q.append((dx,dy,level-1))

arr[lx][ly] = -1
print(bfs_L(lx,ly,-1))

# 0 0
# 4 0 -> 5로 잘 나오지만..

# 3 1
# 1 4 -> 만나는 지점이 없기에.. None이 뜬다(4가 나와야함)
# 제자리 점프의 경우를 고려해줘야 함!