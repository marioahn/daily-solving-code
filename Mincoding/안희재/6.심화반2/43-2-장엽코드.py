# 1은 새우 2는 오징어
    # 난 2개 bfs로 했는데, 여기선 1개로!!
from collections import deque

def bfs(y,x, target):
    global arr
    need_visit = deque()
    need_visit.append((y,x))
    flag = 1

    while need_visit:
        now = need_visit.popleft()
        now_y, now_x = now[0], now[1]

        if target == 1: # 새우는 세 칸 이상 떨어져 있어야한다. 
            direct_y = [-1,1,0,0,-2,2,0,0] # 1, 2 거리 사이에 있으면  fail
            direct_x = [0,0,-1,1,0,0,-2,2]

            for i in range(8):
                new_y = direct_y[i] + now_y
                new_x = direct_x[i] + now_x

                if 0 <= new_y < 7 and 0 <= new_x < 7:
                    if visited[new_y][new_x] == 1: continue
                    if arr[new_y][new_x] == 1:
                        flag = 0
                        return flag
                    visited[new_y][new_x] = 1
                    need_visit.append((new_y, new_x))

        if target == 2: # 오징어는 네 칸 이상 떨어져 있어야 한다.
            direct_y = [-1,1,0,0,-2,2,0,0,-3,3,0,0] # 1, 2, 3 거리 사이에 있으면 fail
            direct_x = [0,0,-1,1,0,0,-2,2,0,0,-3,3]

            for i in range(12): 
                new_y = direct_y[i] + now_y
                new_x = direct_x[i] + now_x

                if 0 <= new_y < 7 and 0 <= new_x < 7:
                    if visited[new_y][new_x] == 1: continue
                    if arr[new_y][new_x] == 2:
                        flag = 0
                        return flag
                    visited[new_y][new_x] = 1
                    need_visit.append((new_y, new_x))
    return flag

arr = [list(input()) for _ in range(7)]

for i in range(len(arr)):
    for k in range(len(arr[i])):
        arr[i][k] = int(arr[i][k])


visited = [[0]*7 for _ in range(7)]
for i in range(len(arr)):
    for k in range(len(arr[i])):
        if arr[i][k] != 0:
            if visited[i][k]== 1: continue
            visited[i][k] = 1
            target = arr[i][k]
            flag = bfs(i,k,target)


if flag:
    print('pass')
else:
    print('fail')