import copy
arr = [list(input()) for _ in range(4)]
N = int(input()) # 폭탄 갯수
# 와; 이거 dfs.. 처음 봤을 때, dfs문제라는 것을 바로 캐치하긴 힘들듯. 계속 보기
# 0. level은 N
# 1. 조합 / 2. direct

# kill한 적군 수를 리턴하고, "동시에" 맵을 청소하는 함수
def bomb(x,y): 
    cnt = 0
    directx = [-1,1,0,0,0] # 상,하,좌,우,타겟(본인)
    directy = [0,0,-1,1,0]
    for i in range(5):
        dx, dy = x+directx[i], y+directy[i]
        if 0 <= dx < 4 and 0 <= dy < 4 and arr[dx][dy] != '_': # 배열범위 내에 적군이 있다면,
            cnt += 1 # kill한 적군 수 세기
            arr[dx][dy] = '_' # 무인지대로 만들기
    return cnt

# 먼저, 알파벳과 좌표를 전부 enemy 리스트로 옮기기
enemy = []
for i in range(4):
    for j in range(4):
        if 65 <= ord(arr[i][j]) <= 90:
            enemy.append([i,j, arr[i][j]]) # [0,0,'A'], [0,1,'B'] ...

path = [''] * N
Max = 0
result = [] # 여기때문에 path랑 같이 바뀌는 것일수도
def dfs(start,level,kill):
    global Max, result, arr
    if level == N:
        if Max < kill:
            Max = kill
            path.sort() # 여기를 먼저 해줘야함. result는 'A H E' 이런 상태라, sort를 쓸 수가 없음(에러)
            result = ' '.join(path) # deepcopy안쓰려고 이렇게 했음!
        return

    tmp = copy.deepcopy(arr)
    for i in range(start,len(enemy)):
        path[level] = enemy[i][2]
        dfs(i+1,level+1,kill+bomb(enemy[i][0],enemy[i][1]))
        arr = copy.deepcopy(tmp)
            
dfs(0,0,0)
print(result)