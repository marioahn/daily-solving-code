from collections import deque
arr = [list(map(int, input().split())) for _ in range(5)]
visit = [[0] * 8 for _ in range(5)]
cnt=0

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        nowx,nowy=q.popleft()
        directx=[-1,1,0,0]
        directy=[0,0,-1,1]

        for i in range(4):
            dx=directx[i]+nowx
            dy=directy[i]+nowy

            if 0<=dx<5 and 0<=dy<8:  # 배열 범위
                if arr[dx][dy]==0: continue # 섬이 아닐경우
                if visit[dx][dy]==1: continue # 이미 방문한 곳이라면
                visit[dx][dy]=1 # 방문체크
                q.append((dx,dy))

for i in range(5):
    for j in range(8):
				# 섬하나 발견했으니, (1)cnt+=1 / (2)visited 체크 / (3)bfs 돌리기!
        if arr[i][j]==1 and visit[i][j]==0: # 섬체크가 되어 있고 방문한 적이 없다면
            cnt+=1
            visit[i][j]=1
            bfs(i,j)

print(cnt)