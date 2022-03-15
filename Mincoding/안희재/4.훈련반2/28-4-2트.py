# 아. 재귀로 푸는건가? DFS탐색은?
n = int(input())
path = [0]
arr = [0] * n
for i in range(n):
    row = list(map(int,input().split()))
    arr[i] = row

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

