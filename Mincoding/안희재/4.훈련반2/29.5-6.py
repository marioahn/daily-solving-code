arr = [[3,2,5,3], [7,6,1,6], [4,9,2,7]]
n = list(map(int,input().split()))
# n = [1,2,1,2]
for i in range(4):
    for k in range(n[i]):
        tmp = arr[2][i]
        for j in range(2,0,-1):
            arr[j][i] = arr[j-1][i]
        arr[0][i] = tmp

for i in range(3):
    print(*arr[i],sep='')

# 특히, 가운데 for k in range(n[i]) 기억!!