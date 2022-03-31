# DP유형! - DFS로도 가능은 하겠지만, 데이터가 커지면 무조건 DP로 풀어야함
# DP유형 만날때마다 잘 기억해두자
# +2,+3 or *2 -> 딱 봐도 *2는 거꾸로 거슬러올라가는게 더 편하겠지 ㅇㅇ.
    # 홀수인덱스는 곱하기 바로 패스되고!

arr = list(map(int,input().split()))
accu = [0] * len(arr) # 그냥 arr길이만큼만. 
accu[0], accu[1] = arr[0], arr[1] # 초기값 설정-> 0번칸부터 최소+2이므로 accu[1]은 밟을 수는 없음. 역추적은 가능해도.
for i in range(2,len(arr)): # accu[0]은 당연히 0이므로. 이전 데이터가 아예 없으니 누적도 0
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

# 아 이게 아니지;;;;;;;;;;;; 꼭 어디가 틀렸는지 다시보기
# 8번째줄의 초기값 설정이 잘못 되었음. 
# 처음에 idx=2일때, idx=1인경우에서 갈 수 있다고 생각해서 넣어놧는데
# 다시 보니까, 애초에 1은 밟을수가 없으므로, 역추적해서 밟힐수가 없는 것임;;; => 아예 빼야됨.. 걍 낚시임..
# arr[1]이 되는 i-2,i-3, i//2는 바로 continue시켜줘야함 ㅠ
# 2트에서 ㄱㄱ
# 아니 그냥 accu[1]을 0으로 두면 되지 않나?