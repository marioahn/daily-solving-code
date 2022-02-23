# 아. 4*4이상부터는 테두리말고, 안에까지 회전시켜야 하는데,
# 이전까지 했던 나의 노가다 풀이로는 절대 풀 수 없다
# 4*4 보면, 1행이 3열, 2행이 2열, 3행이 1열, 4행이 0열로 바꾸면,
# 내부까지 90도 회전이 되네 ㄷㄷ;;;
arr = [[9,5,1,4,3], [2,8,4,7,6], [1,3,0,9,5], [4,6,7,3,1], [2,5,8,9,0]] # 이거 밖에다 둬야지

T = int(input())
for tc in range(T):

    # 1. 일단, 좌표와 M 입력받으면 그걸 arr에 넣는 코드
    x, y, M = map(int,input().split())
    original = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            original[i][j] = arr[x+i][y+j]

    # 2. original을 90도 회전시킨, ret 배열 완성
    ret = [[0] * M for _ in range(M)]
    for r in range(M):
        for c in range(M):
            ret[c][M-1-r] = original[r][c]

    # 3. ret을 arr에 이식하는 작업
    for i in range(M):
        for j in range(M):
            arr[x+i][y+j] = ret[i][j]

# 2번실행시키면, 2번 바뀐 후의 최종 결과(arr의)를 print
for i in range(5):
    print(*arr[i])