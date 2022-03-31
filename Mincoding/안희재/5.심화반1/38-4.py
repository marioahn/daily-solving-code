# 이건 한 코드가 괜춚!
N = int(input())
# 언제까지 돌려? N이면 한 줄에 총 N번 돌릴 수 있음(N+1번은 맨 처음이랑 같음!)
# 즉, N*N의 경우 -> level은 N행까지 즉, N
def move(list): # 오른쪽으로 한번 move
    tmp = list[-1]
    for i in range(len(list)-1,0,-1):
        list[i] = list[i-1]
    list[0] = tmp
    return list

arr = [list(map(int,input().split())) for _ in range(N)]
path = [0] * N
Max = 0

def dfs(level):
    global Max
    if level == N:
        Gop = 1
        for i in range(N):
            Sum = 0
            for j in range(N):
                Sum += path[j][i]
            Gop *= Sum
        if Gop > Max:
            Max = Gop
        return

    # 원상복구 코드 +. 어라 아래처럼 하면 안써도 되지않나?
    tmp = arr[level][:]
    for i in range(N):
        path[level] = move(arr[level])
        dfs(level+1)
        arr[level] = tmp

dfs(0)
print(f'{Max}점')
