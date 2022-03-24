from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # [0] for _ ~ 가 아님.

for _ in range(m):
    a, b = map(int, input().split()) 
    graph[a].append(b) # 인접행렬로 배웠는데, 여기서는 이렇게 하는게 더 편한듯. 스킬!

distance = [-1] * (n+1)
distance[x] = 0
q = deque([x])
while q:
    now = q.popleft()

    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

print(distance)