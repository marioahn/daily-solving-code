from collections import deque
N = int(input())
a1,b1,a2,b2 = map(int,input().split())

virus = [(a1,b1,1), (a2,b2,1)]
arr = [[0] * N for _ in range(N)]

def bfs(virus):
    global N, arr
    q = deque(virus)
    
    while q:
        nowx, nowy, level = q.popleft() 
        arr[nowx][nowy] = level # 자기자신부터 전염

        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<N and 0<=dy<N): continue
            if arr[dx][dy] != 0: continue
            arr[dx][dy] = arr[nowx][nowy] + 1 # 본체 주위는 '본체+1' // level+1로 해도 ㅇㅋ
            q.append((dx,dy,level+1))

bfs(virus) # 초기값

for i in range(N):
    print(*arr[i],sep='')
