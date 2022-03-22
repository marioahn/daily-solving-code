# 아.....이거 backtracking?? 하하하 어캐 푸냐 허허허
# 나 brute force(완전탐색)인데 ㅎㅎ;

n = int(input())
number = list(map(int,input().split()))
operator = ['!!', '#', '$', '&']

def new(a,b,ele):
    if ele == '!!':
        return (a-b)*(a+b)
    if ele == '#':
        if a >= b:
            return a
        else:
            return b
    if ele == '$':
        return (a**2) - (b**2)
    if ele == '&':
        return (a+b)**2

# level = N-1 (3개면 연산자 2개들어가니까)
path = [''] * (n-1)
cnt = 0

def dfs(level):
    global cnt
    if level == n-1:
        tmp = number[0] # 초기값 설정
        for i in range(1,n):
            result = new(tmp,number[i],path[i-1])
            tmp = result
        if result == 100:
            cnt += 1
        return
    
    for i in range(4):
        path[level] = operator[i]
        dfs(level+1)

dfs(0)
print(cnt)