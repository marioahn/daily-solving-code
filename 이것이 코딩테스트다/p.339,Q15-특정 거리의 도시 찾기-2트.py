from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # [0] for _ ~ 가 아님.

for _ in range(m):
    a, b = map(int, input().split()) 
    graph[a].append(b) # 인접행렬로 배웠는데, 여기서는 이렇게 하는게 더 편한듯. 스킬!


distance = [-1] * (n+1)
distance[x] = 0 

q = deque([x]) # bfs함수 만들 때, bfs(x)를 실행코드로 썼잖아. 그거 대신임
while q:
    now = q.popleft()

    for i in graph[now]:
        if distance[i] == -1: # -1만 하는 이유 : 최단거리니까. 1번은 2,3이랑 연결되어있고 그전 q에서 이미 distance는 1이라서 / 4만 보면 됨 ㅇㅇ.
            distance[i] = distance[now] + 1 # 연결되었으니
            q.append(i)

print(distance)
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4