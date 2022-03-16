# BFS
from collections import deque
arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

n = int(input())
answer = []

def bfs(st):
    global answer
    q = deque()
    q.append(st)

    while q:
        now = q.popleft()
        answer.append(now)

        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)

bfs(n)
print(*answer)