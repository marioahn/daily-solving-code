# 더 다듬었음 -> 그런데, start,end를 안에다 넣으니까 최대가치가 빌딩1개인 경우 오류가남
    # 당연하지 -> 2개부터 세니까.. 

# -----------------------------------------------------
n = int(input()) # 빌딩의 갯수
arr = list(map(int,input().split())) # 각 빌딩들의 가치

accu = [[0]*(n+1) for _ in range(n+1)]
# accu 1행은 1개짜리 모은 결과들의 max / 2행은 2개짜리(->idx13까지만 계산!)
# 3행은 3개짜리(->idx12까지만 계산(12,13,14))
accu[1][1:] = arr[:] # 1개만 받는 경우를 초기값으로 각 세팅
tmp = sum(accu[1][1:3]) # 초기값
accu[2][1] = tmp
start, end = 0, 0

for i in range(2,n+1): # i는 행 = 즉, 빌딩갯수
    for j in range(1,n-i+2):
        if sum(accu[1][j:j+i]) > tmp:
            tmp = sum(accu[1][j:j+i])
            start, end = j-1, j-1+i-1
            accu[i][j] = tmp
        else:
            accu[i][j] = tmp

            # start = j-1
            # end = j-1+i-1

print(accu[n][1])
print(start,end)

