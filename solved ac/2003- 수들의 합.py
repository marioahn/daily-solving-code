# 연속된, 그리고 몇개 연속인지는 안정해진 구간의 합이네
# = 투 포인터
N, M = map(int,input().split())

arr = list(map(int,input().split()))

s = 0
e = 0
sum = arr[0] # 0이 아니라, arr[0]으로!
cnt = 0
while 1:
    if sum < M:
        e += 1
        if e == N:
            break
        sum += arr[e]
    elif sum > M:
        sum -= arr[s]
        s += 1
    else: # sum = M
        cnt += 1
        sum -= arr[s] # 이거 중요!
        s += 1

print(cnt)