# 순서 o, 중복 x
# = 순열
cards = list(map(int,input().split()))
path = [0] * 5
used = [0] * 5

# 어라 backtracking?? ..??? how??
# 아, 그냥 Min,Max를 함수의 인자로 넣어서 ..어..? 아닌데,ㅡ Min,Max두개다 해야하는데..
# Min이 갑자기 커졌다고 리턴시켜버리면 Max 못 구하잖아 그 path에서;
Min, Max = 2e18, 0
def abc(level):
    global Min, Max
    if level == 5:
        if (path[0]*path[1]) - (path[2]*path[3]) + path[4] < Min:
            Min = (path[0]*path[1]) - (path[2]*path[3]) + path[4]
        if (path[0]*path[1]) - (path[2]*path[3]) + path[4] > Max:
            Max = (path[0]*path[1]) - (path[2]*path[3]) + path[4]
        return

    for i in range(5):
        if used[i] == 0:
            path[level] = cards[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0

abc(0)

print(Max)
print(Min)
