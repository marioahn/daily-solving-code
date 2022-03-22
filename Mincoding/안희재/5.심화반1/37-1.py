N, M = map(int,input().split())
arr = list(map(int,input().split()))

# 7개에서 3개뽑는 조합 + 최솟값
path = [0] * M
Min = 2e18
answer = 0
def dfs(level,start,Gop):
    global Min, answer
    if level == M:
        if Gop < Min:
            Min = Gop
            # answer = path -> 이렇게 하면 걍 둘다 바뀜 ㅠㅅㅂ..... 1차원 배열도 이렇게 하면 안댐 ㅠ
            answer = path[:] # 이렇게.. 얕은 복사화!
        return

    for i in range(start,N):
        path[level] = arr[i]
        dfs(level+1,i+1,Gop*arr[i])
        # path[level] = 0 굳이..ㅇㅇ;

dfs(0,0,1)
answer.sort()
print(*answer)