from collections import deque
arr = [list(map(int,input().split())) for _ in range(4)]
visit = [[0] * 9 for _ in range(4)]

def bfs(x,y):
    global target, cnt
    q = deque()
    q.append((x,y))

    while q:
        nowx,nowy = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<4 and 0<=dy<9): continue
            if visit[dx][dy] == 1: continue # 재방문ㄴㄴ
            if arr[dx][dy] != target: continue
            cnt += 1
            arr[dx][dy] = -1 # 박멸
            visit[dx][dy] = 1 # 방문체크
            q.append((dx,dy))

Max, answer = 0, 0
for i in range(4):
    for j in range(9):
        cnt = 0
        if arr[i][j] == -1: continue
        target = arr[i][j] 
        bfs(i,j)
        if Max < cnt:
            Max = cnt
            answer = target

print(answer*Max)