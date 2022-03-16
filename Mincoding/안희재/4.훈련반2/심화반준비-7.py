names = input().split()
path = [''] * 3

def abc(level):
    if level == 3:
        print(*path)
        return

    for i in range(3):
        path[level] = names[i]
        abc(level+1)

abc(0)