# 2트 - used배열 사용해서 사이클 잡음
A, B = map(int,input().split())
arr = [
    [0,0,1,0,1,1],
    [1,0,0,1,0,0],
    [0,0,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0]
]

cnt = 0
path = []
used = [0] * 6
used[A-1] = 1 # used[0]이 아니지

def abc(level):
    global cnt, path
    if level == B-1:
        path.append(cnt)

    for i in range(6):
        if arr[level][i] == 1:
            if used[i] == 0:
                used[i] = 1
                cnt += 1
                abc(i)
                used[i] = 0
                cnt -= 1

abc(A-1)
if len(path) > 0:
    print(min(path))
else:
    print(0)
