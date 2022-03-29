from collections import deque
arr = [list(map(int,input().split())) for _ in range(4)]

firecracker = []
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1:
            firecracker.append((i,j,1))

def bfs(firecracker):
    global arr, level
    q = deque(firecracker)

    while q:
        nowx, nowy, level = q.popleft()
        directx = [-1,-1,-1,0,0,1,1,1]
        directy = [-1,0,1,-1,1,-1,0,1]
        for i in range(8):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<4 and 0<=dy<5): continue
            if arr[dx][dy] >= 1: continue
            arr[dx][dy] = level
            q.append((dx,dy,level+1)) # 처음 level이 1로 시작하기에, 


bfs(firecracker)
print(level-1) # 여기서 -1! 
# level변수를 통해, 횟수 카운트 가능!