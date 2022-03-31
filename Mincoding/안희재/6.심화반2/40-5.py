# start, end index -> 즉, 빌딩은 일단 무조건 연결되어서 받아야 함
n = int(input()) # 빌딩의 갯수
arr = list(map(int,input().split())) # 각 빌딩들의 가치

accu = [[0]*(n+1) for _ in range(n+1)]

accu[0][1:] = arr[:]
arr[-1] = 100
# for i in range(n):
#     Max, Max_s, Max_e = 0, 0, 0
#     s, e = 0, i+1 # i는 0부터 시작하니까..
#     for j in range(n+1-i):
#         s, e = s+j, e+j
#         if Max < sum(arr[s:e]):
#             Max = sum(arr[s:e])
#             Max_s, Max_e = s, e
#     accu[i][0], accu[i][1], accu[i][2] = Max, Max_s, Max_e

print(accu)
print(arr)