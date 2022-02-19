# 첫 줄의 1의 개수를 새고, 그 횟수가 1차 포문 횟수
# 사다리타기 원리가 들어간 함수를 각 적용한 결과,
# 끝이 2가 걸리면 그 시작점을 리턴(1차포문의 i인덱스)

# 일단 맨 처음엔 무조건 아래로 내려갈 수밖에 없음(사다리게임 특성상)
    # 내려가면서 좌,우 확인해서 1이 있으면 그 방향으로 +1 or -1
    # 만약, 0이 나옴? 그럼 이제 아래로 가라는 소리
    # 언제까지? while x < 100 

arr = [list(map(int,input().split())) for _ in range(100)]

answer = 0
for i in range(100):
    (x, y) = (0, i)
    if arr[0][i] == 1: #이제 여기서부터 시작
        while x < 100:
            x += 1
            if arr[x][y+1] == 1: # 끝 사다리의 경우 문제인데..?
                while arr[x][y] == 0:
                    y += 1
            elif arr[x][y-1] == 1: # 처음 사다리의 경우 문제인데..?
                while arr[x][y] == 0:
                    y -= 1
        if arr[x][y] == 2:
            answer = i
        
print(answer)


