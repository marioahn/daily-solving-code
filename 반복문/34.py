arr = [[3,6,8,3], [4,7,5,8], [9,5,3,7], [3,2,6,0]]

# 행이 1이면 : arr[0][0] ... arr[0][3]
# 행이 2이면 : arr[1][0] ... arr[1][3]
#..행이 4면 : arr[3][0] ... arr[3][3]

# 열이 5면 : arr[0][0] ... arr[3][0]
# 열이 6이면 : arr[0][1] ... arr[3][1]
# .. 열이 8이면 : arr[0][3] ... arr[3][3]

N, M, O, P = map(int,input().split())

# N, M 행 스왑
for i in range(4):
    arr[N-1][i], arr[M-1][i] = arr[M-1][i], arr[N-1][i]
# O, P열 스왑
for i in range(4):
    arr[i][O-5], arr[i][P-5] = arr[i][P-5], arr[i][O-5]

for i in range(4):
    print(*arr[i])
