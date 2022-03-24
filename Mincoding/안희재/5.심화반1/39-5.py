import copy
# 중복조합
# 4회만에 ooooo or xxxxx가 되는가
meat = list(input())

def flip(x): # 뒤집기 함수 - 너무 노가다인데.. 좀 줄일 수 없나?
    if x-1 >= 0 and x+1 < len(meat):
        if meat[x-1] == 'O':
            meat[x-1] = 'X'
        else: meat[x-1] = 'O'
        if meat[x+1] == 'O':
            meat[x+1] = 'X'
        else: meat[x+1] = 'O'
    elif x-1 >= 0:
        if meat[x-1] == 'O':
            meat[x-1] = 'X'
        else: meat[x-1] = 'O'
    else:
        if meat[x+1] == 'O':
            meat[x+1] = 'X'
        else: meat[x+1] = 'O'
    if meat[x] == 'O':
        meat[x] = 'X'
    else: meat[x] = 'O'

# answer = 'possible' -> 필요없음 ㅠ
cnt, Min = 0, 2e18
def dfs(start,level):
    global cnt, Min, meat  # answer빠졌으니 여기도 ㅌㅌ
    if level == 4:
        if meat.count('O') == 0 or meat.count('X') == 0:
            cnt = level+1
            return
        else:
            # answer = 'impossible' -> 필요없음
            return

    tmp = copy.deepcopy(meat)
    for i in range(start,len(meat)):
        flip(i)
        if meat.count('O') == 0 or meat.count('X') == 0:
            cnt = level+1 # 찾으면 여기서 바로 끝!
            if Min > cnt:
                Min = cnt
            return
        dfs(i,level+1)
        meat = copy.deepcopy(tmp)

dfs(0,0)
if cnt == 0:
    print('impossible')
else:
    print(Min)

# 흠;; 애초에 너무 복잡하게 생각할 필요가 없구나
# cnt가 0이 아니면 -> 올클리어가 최소 1번은 나왔다는 뜻이니까, 바로 Min출력해주면 됨!