word = list(input())
path = [word[0]]
arr = []
for i in range(8):
    row = list(map(int,input().split()))
    arr.append(row)

def abc(level):
    sum = 0
    for i in range(8):
        sum += arr[level][i]
    if sum == 0:
        return

    for i in range(8):
        if arr[level][i] == 1:
            path.append(word[i])
            tmp = i
            abc(tmp)

abc(0)
print(*path,sep='')

