# DP유형! - DFS로도 가능은 하겠지만, 데이터가 커지면 무조건 DP로 풀어야함
# DP유형 만날때마다 잘 기억해두자
# +2,+3 or *2 -> 딱 봐도 *2는 거꾸로 거슬러올라가는게 더 편하겠지 ㅇㅇ.
    # 홀수인덱스는 곱하기 바로 패스되고!
    # 1트에서 실패했듯이, -1,-2,//2해서 idx=1이 되는 경우는 continue!

arr = list(map(int,input().split()))
arr.append(0) # 문제에서 arr은 도착 0정보가 없음 -> 추가해주고, accu의 1번인덱스 = 1번번호로 !
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

print(accu)
print(accu[-1])