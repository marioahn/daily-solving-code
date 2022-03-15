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
        if arr[level][i] == 1:
            path.append(i)
            level = i # 아 이게 문제였구나; 그니까 0 2 5 5가 나오지;;
            abc(level)

    if sum == 0:
        return

abc(0)
print(*path)

# 7
# 0 0 1 1 1 0 0 
# 0 0 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0

# 0 2 5 6 3 1 4가 나와야하는데, 0 2 5 5가 나옴. 리턴 잘못 준듯