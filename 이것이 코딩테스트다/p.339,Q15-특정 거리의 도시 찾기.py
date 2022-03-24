# DFS기초문제네 ㅇㅇ! -> ㄴㄴ 틀림.. BFS임
N, M, K, X = map(int,input().split()) # N번까지 / M개의 '단'방향도로 / 최단거리 K / 출발도시 X

# 간선 정보를 인접행렬에 반영하기
arr = [[0] * N for _ in range(N)]
for i in range(M):
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1

answer = []
path = [0] * N
path[X-1] = 2 # 본인
def dfs(level,cnt): # level은 행(도시 번호)
    if cnt == K:
        if path[level] == 0: # 한번도 못 갔다면, 그게 바로 정답!
            answer.append(level+1) # 0번인덱스는 1번도시!
        return # 어찌되었든 k+1레벨은 의미없으니 return으로 재귀 끝내주기

    for i in range(N):
        if arr[level][i] == 1:
            path[i] = 1
            dfs(i,cnt+1)
            path[i] = 0 # 다시 리셋

dfs(X-1,0) # 1번도시는 0번인덱스!
if len(answer) == 0:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])