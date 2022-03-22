n = int(input())

cards =[0,1,2,3,4,5,6,7,8,9]
path = [0] * n

cnt = 0
def abc(level):
    if level == n:
        if sum(path) == 7:
            global cnt
            cnt += 1
            return
        else: # 여기도 return 꼭 해줘야지
            return

    for i in range(len(cards)):
        path[level] = cards[i]
        abc(level+1)

abc(0)
print(cnt)