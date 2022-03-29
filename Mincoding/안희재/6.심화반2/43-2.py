# 각각 flood fill돌려서, 최초로 만나는(제일 가까운)것과의 거리 판별!(여기서 return)
# 오징어, 새우의 경우로 나눠서 bfs도 2개 만들었는데.. 음.. 더 깔끔하고, 간단하게 how?
from collections import deque
arr = [list(input()) for _ in range(7)]

# 1.새우와 오징어의 각 좌표들을 모두 받기 -> sx,sy가 될 예정
shirmp, squid = [], []
for i in range(7):
    for j in range(7):
        if arr[i][j] == '1':
            shirmp.append((i,j))
        if arr[i][j] == '2':
            squid.append((i,j))

# 2.새우체크용 bfs
def bfs1(x,y,level):
    global cnt
    q = deque()
    q.append((x,y,level))

    while q:
        nowx, nowy, level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<7 and 0<=dy<7): continue
            if visit[dx][dy] == '-1': continue
            if arr[dx][dy] == '1':
                level += 1
                cnt = level
                return
            visit[dx][dy] = '-1'
            q.append((dx,dy,level+1))

# 3.오징어체크용 bfs
def bfs2(x,y,level):
    global cnt
    q = deque()
    q.append((x,y,level))

    while q:
        nowx, nowy, level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<7 and 0<=dy<7): continue
            if visit[dx][dy] == '-1': continue
            if arr[dx][dy] == '2':
                level += 1
                cnt = level
                return
            visit[dx][dy] = '-1'
            q.append((dx,dy,level+1))

answer = 'pass'
sx, sy = 0, 0
for i in range(len(shirmp)):
    cnt = 0
    visit = [[0] * 7 for _ in range(7)]
    sx, sy = shirmp[i][0], shirmp[i][1]
    visit[sx][sy] = '-1'
    bfs1(sx,sy,0)
    if cnt < 3:
        answer='fail'
        break

for i in range(len(squid)):
    cnt = 0
    visit = [[0] * 7 for _ in range(7)]
    sx, sy = squid[i][0], squid[i][1]
    visit[sx][sy] = '-1'
    bfs2(sx,sy,0)
    if cnt < 4:
        answer='fail'
        break

print(answer)