N = int(input()) # N*N
arr = [list(map(int,input().split())) for _ in range(N)]
used = [[0] * N for _ in range(N)]
flag = 0
# 출발지점은 0,0 / 도착지점은 N-1,N-1

def dfs(x,y):
    global flag
    if x == N-1 and y == N-1:
        flag = 1
        return

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if arr[nx][ny] != 1 and used[nx][ny] != 1: # 벽이 아니고 + 이전에 방문한 곳이 아니면,
                used[nx][ny] = 1
                dfs(nx,ny)

used[0][0] = 1
dfs(0,0)
if flag: print('가능')
else: print('불가능')