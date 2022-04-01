# 걍 1행부터 세자
    # 아 근데 굳이 2차배열 만들 이유가 있나?
    # 걍 1차원배열 (n+1)칸 만들고, 1번인덱스에 1개의 최대값 넣는 식으로 하면 되잖아;;
    # 1차원도 아니네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋtime limit 오우쓋;;(메모리는 accu를 1차원으로 만들면서 해결)
    # 답 출력자체는 나오긴 함 vsc에서는 ㅠㅠ
    # DP가 이게 아닌가?ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

# -----------------------------------------------------
n = int(input()) # 빌딩의 갯수
arr = list(map(int,input().split())) # 각 빌딩들의 가치
accu = [0] * (n+1) 
accu[1] = max(arr) # 1개만 상속받을 때의 최대값
Max = accu[1]
start, end = arr.index(Max), arr.index(Max) # 여기 필요함 -> 1개상속받을때 최대값인 경우!
# arr = [1, 2, 3, 2, -3, 0, 1, -8, 3, 2, 3, -1, 2, -3]
for i in range(2,n+1):
    tmps, tmpe = 0, 0+i# 각 행의 초기값
    tmpsum = sum(arr[tmps:tmpe]) 
    for j in range(1,n-i+1): # 바로 위에서 초기값 정했으니 1부터
        if sum(arr[j:j+i]) > tmpsum:
            tmps, tmpe, tmpsum = j, j+i, sum(arr[j:j+i])
    if Max < tmpsum:
        Max = tmpsum
        start, end = tmps, tmpe-1 # 이때의 Max가 최대Max면 더 변하지않을거고, start/end도 그대로! // end는 -1해줘야함
    accu[i] = Max

print(accu)
print(Max)
print(start,end)

# 아 더 줄일수있나..? 그니까 아예 계산할 필요없는 경우 continue로! 하면 시간초과 덜할듯??