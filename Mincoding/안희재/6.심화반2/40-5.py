# start, end index -> 즉, 빌딩은 일단 무조건 연결되어서 받아야 함
n = int(input()) # 빌딩의 갯수
arr = list(map(int,input().split())) # 각 빌딩들의 가치

accu = [[0]*(n+1) for _ in range(n+1)]
# accu 1행은 1개짜리 모은 결과들의 max / 2행은 2개짜리(->idx13까지만 계산!)
# 3행은 3개짜리(->idx12까지만 계산(12,13,14))
accu[1][1:] = arr[:] # 1개만 받는 경우를 초기값으로 각 세팅

for i in range(2,n+1): # i는 행 = 즉, 빌딩갯수
    accu[i][1] = sum(accu[1][1:1+i])
    tmp = accu[i][1]
    for j in range(2,n-i+2):
        if sum(accu[1][j:j+i]) > tmp:
            tmp = sum(accu[1][j:j+i])
            accu[i][j] = tmp
        else:
            accu[i][j] = tmp

Max = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if accu[i][j] > Max:
            Max = accu[i][j]

start, end = 0, 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if accu[i][j] == Max:
            start = j-1
            end = j-1+i-1
            break
    if start != 0:
        break

print(Max)
print(start,end)

# 알고는 있었습니다.. 이 방법이 아니란 것을.....ㅠ