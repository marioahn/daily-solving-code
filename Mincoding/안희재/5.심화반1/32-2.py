# 순위가 바뀔 때.마.다만 한 줄씩 출력하는 거네..
# 아, 일단 n번 돌려서, tmp에 각각 추가시키고,
# 그때마다 각 tmp를 정렬시킨 결과를 [0:3]으로 출력하면 될듯
    # 또한, tmp가 바뀌지 않으면 출력xx
n = int(input())
arr = [input().split() for _ in range(n)]
tmp = []

for i in range(n):
    tmp.append(arr[i])
    if i > 0 and arr[i-1][0] == arr[i][0]:
        tmp[i-1], tmp[i] = tmp[i], tmp[i-1]
    result = sorted(tmp,key=lambda x: int(x[1]),reverse=True) 
    # if tmp[0:3] != result[0:3]:
    #     print(*result[0:3])
    print(*result[0:3])

# 음;; 나중에!


