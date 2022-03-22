n = int(input()) # n*n사이즈
arr = [list(map(int,input().split())) for _ in range(n)]

Max = -2e18
def dfs(level, Gop):
    global Max
    if level == n:
        if Max < Gop:
            Max = Gop
        return

    for i in range(n):
        dfs(level+1, Gop*arr[level][i])

dfs(0,1) # Gop = 1
print(Max)