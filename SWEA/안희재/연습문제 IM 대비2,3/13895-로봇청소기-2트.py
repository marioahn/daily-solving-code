N, M = map(int,input().split()) # N은 행, M은 열
r, c, d = map(int,input().split()) 
arr = [list(map(int,input().split())) for _ in range(N)] # 0 : 빈칸, 1: 벽
cnt = 1 # 청소한 칸의 수 - 등장칸 청소하고 시작하니, 1부터
arr[r][c] = 2 # 청소하면 2로 바꾸고, 등장칸은 일단 청소하고 보는 거지


# d는 바라보는 방향이며, 0(북), 1(동), 2(남), 3(서)
x, y = r, c # x, y는 현재 위치(계속 갱신시킬 것임)


# 1 1 1 1 1 1 
# 1 0 0 0 0 1
# 1 1 1 0 0 1 
# 1 0 2 0 0 1
# 1 0 0 0 1 1
# 1 1 1 1 1 1
r, c = (3,2)
N, M = 6, 6

# 1 1 1 1 1 1 
# 1 2 2 2 0 1
# 1 1 1 2 2 1 
# 1 2 2 2 2 1
# 1 2 2 2 1 1
# 1 1 1 1 1 1

8 + 4 + 6 + 6 + 8 + 7 + 6 + 6 + 8
59