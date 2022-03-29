from collections import deque # BFS!
N,N = map(int,input().split()) # N*N
arr = [list(map(int,input().split())) for _ in range(N)]
x,y = map(int,input().split())
# 값이 1 or 배열범위 벗어나는 경우 or 숫자가 이미 차있는 경우 continue
# 처음 레벨은 0!
# grill = [(x,y,0)]

def bfs(grill):
    global N, arr, level
    q = deque(grill)

    while q:
        nowx, nowy, level = q.popleft()
        arr[nowx][nowy] = level

        directx = [-1,1,0,0]
        directy = [0,0,-1,1]
        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<N and 0<=dy<N): continue
            if arr[dx][dy] > 0: continue
            arr[dx][dy] = level+1
            q.append((dx,dy,level+1))

bfs([(x,y,0)]) # 어라; [x,y,0] 하니까 안되네..? 한번더 감싸줘야 함. 안 그러면,
# TypeError: cannot unpack non-iterable int object 뜸..
print(level)