# 1. 섬크기 찾고, 더 작은 거를 기준으로.
# 2. 더 작은 사람의 모든 좌표 돌려서, 큰 사람의 #와 최단거리로 몇?
# 3. 그리고 각 좌표들의 최단거리의 Min값 찾기
# 좌표시작은 왼쪽아래 / 우측위부터 시작 ㅇㅇ
from collections import deque
arr = [list(input()) for _ in range(8)]

# 1. 아래사람 좌표들을 bfs로 넣기
low = [(7,0)]
def bfs1(x,y,level):
    global low
    q = deque()
    q.append((x,y,level))

    while q:
        nx,ny,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]
        for i in range(4):
            dx = nx + directx[i]
            dy = ny + directy[i]
            if not(0<=dx<8 and 0<=dy<9): continue
            if arr[dx][dy] != '#' or arr[dx][dy] == '0': continue
            arr[dx][dy] = '_' # 다른 사람과 구별해주기 위해서 바꿔줌
            low.append((dx,dy))
            q.append((dx,dy,level+1))

arr[7][0] = '0'
bfs1(7,0,0)

def bfs2(x,y,level):
    global cnt
    q = deque()
    q.append((x,y,level))
    while q:
        nx,ny,level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]
        for i in range(4):
            dx = nx + directx[i]
            dy = ny + directy[i]
            if not(0<=dx<8 and 0<=dy<9): continue
            if visit[dx][dy] == 1: continue
            if arr[dx][dy] == '#':
                cnt = level
                return
            visit[dx][dy] = 1 # 재방문 방지용 코드
            low.append((dx,dy))
            q.append((dx,dy,level+1))

sx,sy, Min = 0, 0, 2e18
for i in range(len(low)):
    visit = [[0] * 9 for _ in range(8)]
    cnt = 0
    sx, sy = low[i][0], low[i][1]
    bfs2(sx,sy,0)
    Min = min(Min,cnt)

print(Min)
