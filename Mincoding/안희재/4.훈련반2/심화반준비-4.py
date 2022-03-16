arr = [list(map(int,input().split())) for _ in range(6)]
name = ['A','B','C','D','E','F']
path = ['A']

def dfs(level):
    for i in range(6):
        if arr[level][i] == 1:
            path.append(name[i])
            dfs(i)
            path.pop()
    if sum(arr[level]) == 0:
        print(*path,sep='')

dfs(0)