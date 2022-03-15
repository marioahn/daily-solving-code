# 1트 - 이거 왜 안되는거지..? 논리는 구현한것 같은데
# 아니 근데, cnt >= 5 이 제한 숫자를 정하기가 어려울듯..
# 일단 used 안 쓰기도 했고. 이건 패스
# used를 안 쓰면 무한사이클된다. 
arr = [
    [0,0,1,0,1,1],
    [1,0,0,1,0,0],
    [0,0,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0]
]
A, B = map(int,input().split())
cnt = 0
path = []

def abc(level):
    global cnt
    if cnt >= 5: # 무한 반복 사이클 방지용
        return

    for i in range(6):
        if arr[level][i] == 1:
                cnt += 1
                if i == B-1:
                    path.append(cnt)
                abc(i)
                cnt -= 1

abc(A-1)
print(path)
