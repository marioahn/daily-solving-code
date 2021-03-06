# 복도에 각 구간이 있다고 가정
# 복도 200칸(no.1~200)이 있으며, 룸1,2는 복도 no.1에 속함 / 룸3,4는 복도no.2 / ... 룸399,400은 복도no.200
# 학생 수만큼, 반복문을 돌려서 각 학생이 복도 구간을 지나갈 때 마다 +1
# 복도 버킷중, 가장 큰 값 = 구간이 겹.치는 모.든 학생이 순서대로, 그 구간을 지날 수 밖에 없었다
    # 최댓값 구하는게 훨씬 편하다. 어차피, 덜 겹치는 구간은 고려할 여지가 적으므로
# 복도 버킷 만들기
    # (1, 100) -> no.1부터 no.50까지 + 1
    # (3, 11) -> no.2부터 no.6까지 + 1

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    corridor = [0] * 200
    for i in range(N):
        if arr[i][0] > arr[i][1]:
            arr[i][0], arr[i][1] = arr[i][1], arr[i][0] # 30, 20인경우 -> 20, 30으로
        s = (arr[i][0]//2) - 1 # index이므로 -1. no.1칸은 corridor의 0번칸
        e = (arr[i][1]//2) - 1
        if s == -1:
            s == 0

        for j in range(s,e+1): # i번 학생이 지나는 모든 복도구간을 버킷에 표시해줌
            corridor[j] += 1

    print(f'#{tc}', max(corridor))

# 테스트케이스 7/10 ㅆㅃ..............
# 아 씨바;;; arr[i][0]이 1이면 s = -1되고, corridor[-1]는 맨 끝이 되기때문에 마지막이 2가 된다
# 20~23을 아래처럼 고쳐야함

    # s = (arr[i][0] - 1) // 2
    # e = (arr[i][1] - 1) // 2