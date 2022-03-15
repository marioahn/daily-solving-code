arr = [3,1,2,1,3,2,1,2,1]
n = int(input())
path = ['시작']
result = []

tmp = n-1 # 0이 아니지..
def abc(level): # level은 여기서는 index!
    if level >= len(arr):
        path.append('도착')
        result = path
        for i in range(len(path)-2,-1,-1):
            result.append(path[i])
        return

    global tmp
    tmp += arr[level]
    path.append(arr[level])
    abc(tmp)

abc(n-1)

print(*path)