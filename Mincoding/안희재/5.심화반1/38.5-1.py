# 순열.
# 가장 큰 숫자를 가지는 조합의 총 개수를 출력 해주세요.
    # => 리턴조건일때, Gop = Max인 경우를 추가해서 cnt+1 시키기
    # 만약 뉴 페이스면, cnt = 1로 초기화시키고 ㅇㅇ.
# 아아니;;; 순열이 아니라 조합이지 조합..................;;;;
arr = [list(map(int,input().split())) for _ in range(3)]
position = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
used = [0] * 9
Max, cnt = -2e18, 0
def dfs(start,level,Gop):
    global Max, cnt
    if level == 3:
        if Max < Gop:
            Max = Gop
            cnt = 1
        elif Max == Gop:
            cnt += 1
        return

    for i in range(start,9):
        if used[i] == 1: continue
        used[i] = 1
        dfs(i+1,level+1, Gop*arr[position[i][0]][position[i][1]])
        used[i] = 0

dfs(0,0,1)
print(cnt)

# 빽트랙킹 -> 요소가 0이면 당연히 곱하기 0이니까 back..! 조건 추가해주면 됨