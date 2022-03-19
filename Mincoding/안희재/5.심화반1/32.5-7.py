arr = [list(map(int,input().split())) for _ in range(4)]

def rectangle(h, w, x, y): # h,w는 세로,가로 / x, y는 좌표
    Sum = 0
    for i in range(len(dh)):
        for j in range(len(dw)):
            if 0 <= x+dh[i] < 4 and 0 <= y+dw[j] < 8:
                if arr[x+dh[i]][y+dw[j]] == 0:
                    return 0
                else:
                    Sum += arr[x+dh[i]][y+dw[j]]
    return Sum

Max = 0
height, width = 1, 1
for a in range(4):
    for b in range(8):
        height += a
        width += b
        dh = [i for i in range(height)] # 2 * 3이면 dh = [0,1]
        dw = [i for i in range(width)] # dw = [0,1,2]

        for i in range(4):
            for j in range(8):
                if Max < rectangle(height, width, i, j) :
                    Max = rectangle(height, width, i, j)
    
print(Max)

# 0 0 3 3 0 0 1 1
# 2 1 1 2 0 0 2 2
# 1 1 2 3 9 1 3 3
# 0 0 1 1 0 0 4 4
