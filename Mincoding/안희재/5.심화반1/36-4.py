n = int(input())
coins = [10,40,60]
path = []

Min = 2e18
def abc(level, ch):
    global Min
    if ch < 0:
        return

    if ch == 0:
        if level < Min:
            Min = level

    # if level == 1000: -> 원래는 넣어주는게 맞긴 함!!
    #     return

    for i in range(3):
        abc(level+1, ch-coins[i])

abc(0,n)
print(Min)
