# 사이클이지만, 한번 방문했던 노드는 방문 불가
# BFS
from collections import deque
arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0],
]

n = int(input())
path = []
used = [0] * 6
used[n] = 1

def bfs(st):
    global paths
    q = deque()
    q.append(st)

    while q:
        now = q.popleft()
        path.append(now)
        print(now)

        for i in range(6):
            if arr[now][i] == 1:
                if used[i] == 0:
                    q.append(i)
                    used[i] = 1


bfs(n)