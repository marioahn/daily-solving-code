# 12번인덱스 이상 도착할때 얻을 수 있는 최대포인트 
# -> 일단 accu를 11번인덱스(총12칸)까지 구해놓고, 6번인덱스부터 끝까지 중에서 Max 찾기;;
    # 6~11에서 곱하기2 인덱스로 12번인덱스 이상을 도달할 수도 있으므로.. 

arr = list(map(int,input().split()))
accu = [0] * (len(arr)) # accu[-1]은 12번째인덱스고, 도착지점!
accu[0], accu[1] = 0, 0 # 아예 accu[1]를 arr[1]가 아니라 그냥 0으로 줘버리기.
for i in range(2,len(arr)): # accu[0]은 당연히 0이므로. 이전 데이터가 아예 없으니 누적도 2부터 시작. accu칸수가 arr와 같다는걸 이해하자!
    jp1 = accu[i-2] # 여기 arr이 아니라, accu임. arr로 적으면 아예 이 문제를 이해 못한것. DP또한, 마찬가지
    jp2 = accu[i-3]
    jp3 = accu[i//2]

    accu[i] = jp1+arr[i]
    if i-3 >= 0 and accu[i] < jp2+arr[i]:
        accu[i] = jp2+arr[i]
    if i % 2 == 0 and accu[i] < jp3+arr[i]:
        accu[i] = jp3+arr[i]

print(max(accu[6:])) # 근데 이게 결국 맞나? 맞겠지? 논리상 맞을것 같은데 흠..