# 0행이 4열, 1행이 3열, 2행이 2열, 3행이 1열, 4행이 0열
n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def r_rotate(arr):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][i] = arr[n-1-i][j]
    return result

for i in range(k):
    arr = r_rotate(arr)

for i in range(n):
    print(*arr[i])
