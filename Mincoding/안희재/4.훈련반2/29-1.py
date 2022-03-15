n = int(input())
path = [0]
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def abc(level):
    sum = 0
    for i in range(n):
        sum += arr[level][i]
    if sum == 0:
        return

    for i in range(n):
        if arr[level][i] == 1:
            path.append(i)
            tmp = i
            abc(tmp)

abc(0)
print(*path)