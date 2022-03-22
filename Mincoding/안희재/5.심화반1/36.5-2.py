n = int(input()) # n이 레벨
card = [1,2,3,4,5,6,7,8,9]
path = [0] * n

cnt = 0
def dfs(level,sum):
    global cnt
    if sum > 10:
        return
    if level == n:
        if sum == 10:
            cnt += 1
        return
    
    for i in range(9):
        path[level] = card[i]
        dfs(level+1, sum + card[i])

dfs(0,0)
print(cnt)