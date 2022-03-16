# DFS탐색인데, 가중치를 +하라는 문제
arr = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]

sum = 0
n = int(input())
used = [0] * 6
used[n] = 1
path = [[n,0]]
sum = 0

def dfs(now):
    global sum
    for i in range(6):
        if arr[now][i] != 0:
            if used[i] == 0:
                used[i] = 1
                sum += arr[now][i]
                path.append([i,sum])
                dfs(i)
dfs(n)

for i in range(len(path)):
    print(*path[i])
