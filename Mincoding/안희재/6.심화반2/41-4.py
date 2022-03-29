from collections import deque
arr = [list(map(int,input().split())) for _ in range(4)]

size = 0
def bfs(x,y):
    global size
    q = deque()
    q.append((x,y))

    while q:
        nowx,nowy = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<4 and 0<=dy<4): continue
            if arr[dx][dy] == 0: continue
            if visit[dx][dy] == 1: continue # 이미 방문한 곳
            visit[dx][dy] = 1
            q.append((dx,dy))

Max = 0
for i in range(4):
    for j in range(4):
        visit = [[0] * 4 for _ in range(4)] # 여기에 둬야 섬 크기를 각각 구할 수 있음
        if arr[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i,j)
            size = 0
            for i in range(4):
                size += sum(visit[i])
            if Max < size:
                Max = size

print(Max)
# 여기는 1~3번문제들처럼, level로 섬 크기를 구할 수 없음!
# 1 1 1 1
# 0 1 1 1
# 1 1 0 0
# 1 1 0 1 
# 의 경우, 11이 아닌 -> 6이 출력된다. level은 +1하면서 퍼져나가는 식이기 때문.