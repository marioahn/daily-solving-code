# 와 ㅅㅂ.. 그냥 어차피 엘사가 안나(고정)갈때, 그 거리의 //2를 하면 되잖아
def find(start,arrival):
    move = [(*start,0)]
    min_second = 25
    while move:
        y,x,sec = move.pop(0)
        if [y,x] == arrival and min_second > sec:
            min_second = sec
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < 5 and 0 <= nx < 5:
                if ice[ny][nx] ==  visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    move.append((ny,nx,sec+1))

    min_second = (min_second + 1)//2
    print(min_second)

ice = [[0,0,0,1,0],
       [0,0,0,1,0],
       [1,1,0,0,0],
       [0,0,1,0,0],
       [0,0,0,0,0]]
visited = [[0]*5 for _ in range(5)]
elsa = list(map(int,input().split()))
anna = list(map(int,input().split()))
find(elsa,anna)