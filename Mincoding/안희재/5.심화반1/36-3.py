cards = input().split()
path = [''] * 3
used= [0] * 3

def abc(level):
    if level == 3:
        print(*path,sep='')
        return

    for i in range(3):
        if used[i] == 0:
            path[level] = cards[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0

abc(0)