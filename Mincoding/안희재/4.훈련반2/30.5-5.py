word = list(input())
n = int(input())
path = [''] * n

def abc(level):
    if level == n:
        print(*path,sep='')
        return

    for i in range(len(word)):
        path[level] = word[i]
        abc(level+1)
        
abc(0)