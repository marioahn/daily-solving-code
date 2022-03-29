# 애초에 bfs가 최소조건임 ㅇㅇ. 그래서 따로 최소 문 이동횟수를 굳이 안 구하려고 해도 됨
# https://jjudrgn.tistory.com/47 -> 최소조건? => bfs가능성있음!!
# 시작 정점으로 부터 가까운 정점(height가 낮은 곳부터)을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회함으로써 노드를 넓게(wide) 탐색한다.
# BFS는 두 노드 사이의 최소 경로를 구하는 성질이 있어, 주로 '최단 경로',  '최소 몇 번', '최소 이동 횟수', '최소 연산 횟수' 등과 같은 표현이 있는 문제에 주로 사용된다
# 나는, 이 최소 조건때문에 애먹었는데 - 애초에 bfs는 최소
# 아래 코드를 보면, idx가 길이를 넘어서는 최초의 순간 = 최소 cnt
    # 왜냐하면, idx가 늘어나도 cnt는 안 늘어남. cnt는 문을 이동시켜야할때만 억지로 늘어나는 경우
from collections import deque
def bfs(left, right):
    q = deque()
    q.append((left,right,0,0))
    while q:
        door1, door2, idx, cnt = q.popleft()
        move = [-1,1]
        if idx == 12: # 어찌보면 여기가 핵심. ㅇㅇ. 넘어서는 순간이, 최솟값 ㅇ. !!
            print(cnt)
            return
        enter = customer[idx]
        if enter in [door1,door2]:
                for i in range(2):
                    new1 = door1 + move[i]
                    new2 = door2 + move[i]
                    if enter == door1:
                        if 0 <= new1 < 5 and new1 != door2: # 왼쪽문 이동
                            q.append((new1,door2,idx,cnt+1))
                        elif new1 == door2 and 0 <= new2 < 5:
                            q.append((new1, new2, idx, cnt + 2)) # 문 2개 오른쪽 이동 움직인 것이므로
                    elif 0 <= new2 < 5 and new2 != door1: # 오른쪽문 이동
                            q.append((door1,new2,idx,cnt+1))
                    elif new2 == door1 and 0 <= new1 < 5: # 문 2개 왼쪽 이동
                        q.append((new1, new2, idx, cnt + 2))
        else:
            q.append((door1,door2,idx+1,cnt))

customer = [0,1,0,1,0,1,2,3,2,3,2,3]
position = list(map(int, input().split()))
doors = []
for i in range(5):
    if position[i]:
        doors.append(i)
bfs(*doors)