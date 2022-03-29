# 아예 하나에 넣어서 했네 ㄷㄷ;; 내 코드하고 비교해서 봐보기!!
def delivery(*args):
    q = [(*args,0)]
    n = 1
    visited = [[0]*5 for _ in range(3)]
    visited[args[0]][args[1]] = 1
    while q:
        y, x, cnt = q.pop(0)
        idx = info[y][x]
        if n == idx == 4:
            print(f'{cnt}회')
            return
        elif idx == n:
            n += 1
            q = []
            visited = [[0] * 5 for _ in range(3)]
            visited[y][x] = 1
        for dy,dx in (1,0),(-1,0),(0,-1),(0,1):
            ny = y+dy
            nx = x+dx
            if 0 <= ny < 3 and 0 <= nx < 5:
                if info[ny][nx] != '#' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx,cnt+1))

info = ['']*3
check = [0]*5
for i in range(3):
    info[i] = list(map(str,input()))
    for j in range(5):
            if info[i][j] !='#':
                info[i][j] = int(info[i][j])

delivery(0,0)