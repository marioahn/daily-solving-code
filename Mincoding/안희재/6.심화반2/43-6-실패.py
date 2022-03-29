from collections import deque
import copy
# guest를 stack이라고 생각하고 하나씩 뺀다고 생각하면 될듯
# cnt는 문을 움직일때만 하고 -> 한번에 문 1개씩만 이동 가능
# Hint: Queue 노드에는 A의 위치, B의 위치, 몇 번 손님까지 처리했는지 이렇게 정보를 가지고 BFS를 돌리기!
    # 0 1 1 0 0 (시작) : 0 번째 손님 입장 완료
    # 0 1 0 1 0 (총 1회 이동)
    # 0 0 1 1 0 (총 2회 이동) : 1 ~ 5 번째 손님 입장 완료
    # 0 0 1 0 1 (총 3회 이동)
    # 0 1 0 0 1 (총 4회 이동) : 6 ~ 11 번째 손님 입장 완료
# 근데 최소횟수..잖아? 음..?
# 일단 종료조건은 idx가 door길이 넘어설때까지.
# 이게 어떻게 BFS이지.. 흠;;;;;개어렵다.. 생각을 아예 못하겠음

guest = [0,1,0,1,0,1,2,3,2,3,2,3]
door = list(map(int,input().split())) # 문의 초기 상태 - 0 1 1 0 0
closedoor = list(filter(lambda x: door[x] == 1, range(len(door)))) # 미닫이문 인덱스찾기 
a, b = closedoor[0], closedoor[1]

def direction(index,x,y,list): # x,y는 미닫이문 위치, list는 door상태
    # a번문 왼쪽
    tmp1 = copy.deepcopy(list) # door 깊은복사
    cnt1 = index
    if x-1 >= 0:
        tmp1[x-1], tmp1[x] = tmp1[x], tmp1[x-1]
        while 1:
            if tmp1[guest[cnt1]] == 1: break
            else: cnt1 += 1

    # a번문 오른쪽
    tmp2 = copy.deepcopy(list)
    cnt2 = index
    if x+1 != y: # x+1자리에 y가 없다면,
        tmp2[x+1], tmp2[x] = tmp2[x], tmp2[x+1]
        while 1:
            if tmp2[guest[cnt2]] == 1: break
            else: cnt2 += 1

    # b번문 왼쪽
    tmp3 = copy.deepcopy(list)
    cnt3 = index
    if y-1 != x: # y왼쪽에 바로 x가 있다면 왼쪽으로 못감!
        tmp3[y-1], tmp3[y] = tmp3[y], tmp3[y-1]
        while 1:
            if tmp3[guest[cnt3]] == 1: break
            else: cnt3 += 1

    # b번문 오른쪽
    tmp4 = copy.deepcopy(list)
    cnt4 = index
    if y+1 < len(tmp4):
        tmp4[y+1], tmp4[y] = tmp4[y], tmp4[y+1]
        while 1:
            if tmp4[guest[cnt4]] == 1: break
            else: cnt4 += 1

    if max(cnt1,cnt2,cnt3,cnt4) == cnt1:
        list[x-1], list[x] = list[x], list[x-1]
        index = cnt1
    elif max(cnt1,cnt2,cnt3,cnt4) == cnt2:
        list[x+1], list[x] = list[x], list[x+1]
        index = cnt2
    elif max(cnt1,cnt2,cnt3,cnt4) == cnt3:
        list[y-1], list[y] = list[y], list[y-1]
        index = cnt3
    else:
        list[y+1], list[y] = list[y], list[y+1]
        index = cnt4

cnt = 0
def bfs(A,B,idx): # A,B위치, 몇회차인지
    global cnt
    q = deque()
    q.append((A,B,idx))

    while idx < len(guest): # q대신에. 음.. 같이써야하나?
        nowa,nowb,idx = q.popleft()
        doormove = [-1,1] # 가만히 있는 경우는 direct돌리기전에 미리 처리
        # 문 이동순위? - 일단 왼쪽부터 해보자 - 문 이동시켜야하면 cnt+1임
        # 아. 다음인덱스꺼까지 봐서? 거기까지 피해안주는 방향으로 살피면 최소는 나올듯?
        # 아아~ 노노노. 총 4가지 방법이 있지 A왼오 / B왼오 => 4가지 방법 중 guest가 제일 많이 지워지는 거 선택!!
        # 와 ㅋㅋ BFS..이게 BFS구나
        
        # .일단 문 이동시키기전에 현재 상태에서 지워질수 있는지 없는지 보기
        while 1:
            if door[guest[idx]] == 1: break
            else: idx += 1

        # .손님을 최대한 많이 빼도록 미닫이문 이동(A왼,A오,B왼,B오 중에서)
        direction(idx,nowa,nowb,door)
        cnt += 1
        q.append((nowa,nowb,idx))

bfs(a,b,0) # a,b는 미닫이문의 '인덱스' 위치 / 항상 a < b임
print(cnt)