# 경로탐색이므로, 한 번 간곳은 ㄴㄴ. used사용
# 깊이탐색.
arr = [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
]
n = int(input())
used = [0] * 6
used[n] = 1
result = [n]

def dfs(now):
    for i in range(6):
        if arr[now][i] == 1:
            if used[i] == 0:
                used[i] = 1
                result.append(i)
                dfs(i)

dfs(n)
print(*result)