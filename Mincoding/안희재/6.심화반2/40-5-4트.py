# 아. 음수기준으로 나누면 될듯? 그리고 음수구간 건너띌 필요 없으면 음수 사이에서만 보고
# 즉, 먼저 -없는 구간끼리(양의집합)의 최대값 구하고 구간 넘어갈때  그거보다 적으면 구간늘리든지 해서 끝까지 감. IDX가 끝 넘어서면 끝!
# 일단 처음이 양수인 인덱스를 시작점으로 (-1,-2,1) 인경우 1만 뽑으면 됨. s,e는 2,2)
# 음수구간을 넘어서게되는 경우는?? 그 다음 음수구간 < 다음의 양수구간 + (처음구한 양수의 최댓값) 일 경우에?
# 만약 아니라면, 현재 양수구간을 건너띄고 다음 양수구간으로!ㅇㄹㅊㅌ

n = int(input())
arr = list(map(int, input().split()))

def check(ele):
    # 0은..음 .. 일단 양수쪽에 포함시켜두자(index판단시 0이 더 작으면 포함시켜야 하나?)
    if ele >= 0: return 1  
    else: return -1

# 연속된 양수끼리의 합과 음수끼리의합 그리고 각각의 인덱스(연속경우면 연속된 인덱스)를 튜플로 담을 예정
# 일단 초기값: +담을때는 (합,스타트,엔드인덱스) 총 3가지를 담을 예정
accu = [[arr[0], 0, 0]]

# 이전수와 더해서 작아지면 부호바뀐거고, 커지면 그대로 커지는 것
for i in range(1, len(arr)):
    if check(arr[i]) == check(arr[i-1]):
        accu[-1][0] += arr[i]
        accu[-1][2] = i
    else:  # 만약, 부호가 다르면 새로 추가하고, 스타트,엔드정보도 담기
        accu.append([arr[i], i, i])

accu2 = [[0,0,0]] * len(accu)
accu2[0] = [accu[0][0],accu[0][1],accu[0][2]] # 이렇게하면 얕은복사문제 x?

for i in range(1,len(accu2)):
    if accu[i][0] < 0: # 음수라면, 일단 전의 것은 무조건 더해야지(양수일테니까)
        accu2[i] = accu[i]+accu[i-1]
    else: # 만약 양수라면
        # 만약 이전 accu2가 음수라면 그냥 accu2[i] = accu[i]로 하고
        # 아니라면, accu2[i]는 accu[i]+accu2[i-1] !!
