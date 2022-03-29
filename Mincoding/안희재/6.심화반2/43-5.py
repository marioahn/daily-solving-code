# 와.. 이거 bfs로 풀 수 있음. 진짜 개쩐다..
# '//2', '*2', '+1', '-1'를 direct처럼 만들면 될듯?
from collections import deque
start = int(input())
end = int(input())

def bfs(now,level):
    global start, end
    q = deque()
    q.append((now,level))

    while q:
        now,level = q.popleft()
        operator = [now//2,now*2,now+1,now-1]

        for i in range(4):
            if operator[i] == end:
                print(level+1)
                return
            q.append((operator[i],level+1))

bfs(start,0)