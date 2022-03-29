# queue의 핵심은 지금 현재 상태에서 이동(변화)할 수 있는 것을 모드 q에 push(append)하는 것!
# 1. if a도어가 0보다 클때, -> a-1(왼쪽 이동 가능)
# 2. if b도어가 4보다 작다면, -> b+1(오른쪽 이동 가능)
# 3. if (b-a) > 1(붙어 있지 않다면),
    # - a도어 우측 이동한 경우
    # - b도어 좌측 이동한 경우
# 와 이렇게 딱 4가지지; ㄷㄷ;ㄷ;ㄷ;ㄷ;ㄷ;;ㄷㄷ; 
# bfs는 현재 위치에서 갈 수 있는 것을 차례대로 집어넣는데, (너비탐색이잖아. 깊이가 아니라. level+1임 단지)
    # (level+1끼리만 쭉 비교해서 ㄴㄴ? 그럼 그제서야 level+2! 여기서는 문이동횟수가 level이 되겠지)
    # (dfs는 leve+3까지 하고, 그 오른쪽 트리에서 다시 내려오고 이러는건데)
    # (한번에, q.append가 여러개 되는 경우도 있지만 그건 모두 같은 level상(같은 깊이에서 너비만 다른 경우))임 ㅇㅇ.
    # (위 내용을 기억하자!!!)
# 따라서, 리턴조건에 걸려서 return된다면 그게 최소!(물론, 리턴조건을 최소에 맞춰 줘야겠지)
from collections import deque
arr=[0,1,0,1,0,1,2,3,2,3,2,3]
moon=list(map(int, input().split()))
door=[]

def bfs(a,b):
    q = deque()
    q.append((a, b, 0, 0))  # person index   # level(문 몇번)
    while q:
        nowa, nowb, person, level = q.popleft()

        isdoor=[0]*5
        isdoor[nowa]=1
        isdoor[nowb]=1

        if person==12: # (여기로 인해, 최소 cnt를 그려낼 수 있는 겄!)
            return level

        if isdoor[arr[person]]!=1: #만약에 사람이 들어가려고 하는 곳에 문이 없다면
            q.append((nowa,nowb,person+1,level))
            continue

        if nowa>0:
            q.append((nowa-1,nowb,person,level+1))  # 문 a의 위치가 0번이 아니라면(크다면) 왼쪽으로 이동 가능
        if nowb<4:
            q.append((nowa,nowb+1,person,level+1)) # 문 b의 위치가 4번이 아니라면(작다면) 오른쪽으로 이동 가능
        if (nowb-nowa) > 1: # 두 문이 붙어있지 않는경우
            q.append((nowa+1,nowb,person,level+1)) # 문 a의 위치 오른쪽으로 이동 가능
            q.append((nowa,nowb-1,person,level+1)) # 문 b의 위치 왼쪽으로 이동 가능

for i in range(5):
    if moon[i] == 1:
        door.append(i)  # 몇번 인덱스에 문 a,b 가 있는지 door에 체크 한 후 bfs로 넘기기

answer=bfs(door[0],door[1])
print(answer)