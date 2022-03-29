# 오우ㅠ;; 굿

def dfs(arg=0,total=0):
    global max_val,prey
    if arg >= 3 * turn:
        if total > max_val:
            max_val = total
        return
    if arg!=0 and arg%3 == 0:
        backup = prey[:]
        for i in range(6):
            if prey[i]:
                prey[i] *= 2
    start, end = idx_lst[arg%3]
    for i in range(start,end):
        eat = prey[i]
        prey[i] = 0
        dfs(arg+1,total+eat)
        prey[i] = eat
    if arg!=0 and arg%3 == 0:
        prey = backup

prey = list(map(int, input().split()))
turn = int(input())
idx_lst = [[0,3],[3,6],[1,5]]
max_val = 0
dfs()
print(max_val)