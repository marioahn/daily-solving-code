n = int(input())
result = ['o','x']
path = []

def abc(level):
    if level == n:
        print(*path,sep='')
        return

    for i in range(len(result)):
        path.append(result[i])
        abc(level+1)
        path.pop()

abc(0)