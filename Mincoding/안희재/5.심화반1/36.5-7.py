# 순서대로 줄세우기 - 순열
# 총 6자리이고, 그 중에서 a,b자리는 못 들어가니까(4)
# 경우의 수는 (6-2) * (5*4*3*2*1) = 480
animals = ['A', 'B', 'C', 'D', 'E', 'F']
# 'E'가 뽀삐라고 하자
a, b = map(int,input().split())
path = [0] * 6
used = [0] * 6

cnt = 0
def dfs(level):
    if path[a-1] =='E':
        return
    if path[b-1] == 'E':
        return
    
    if level == 6:
        global cnt
        cnt += 1
        return
    
    for i in range(6):
        if used[i] == 0:
            path[level] = animals[i]
            used[i] = 1
            dfs(level+1)
            used[i] = 0
            path[level] = 0 # 여기 꼭 넣어줘야 함!!!!! - 중복x니까 ㅇㅇ;;빼줘야지! node에서 나오면

dfs(0)
print(cnt)
