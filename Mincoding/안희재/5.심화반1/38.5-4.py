import copy
# 0.중복조합문제 - 최대6번까지만 가능. level 6번 넘어가면 return
    # 중간에 가로 AAA가 발견되면 바로 answer = '가능'으로 바꾸고 return
# 1.테두리는 불가능 -> 일단 선택가능한 좌표부터 구해야지

N = int(input())
arr = [list(input()) for _ in range(N)]

# (1)3*3의 테두리를 회전시키는 함수
def rotate(x,y): # x,y를 중심으로 테두리 회전(3*3배열)
    arr1 = [[x+1,y-1],[x,y-1],[x-1,y-1], [x+1,y],[x,y],[x-1,y], [x+1,y+1],[x,y+1],[x-1,y+1]] # rotate
    arr2 = [[0] * 3 for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            arr2[i][j] = arr[arr1[k][0]][arr1[k][1]] 
            k += 1
    a = 0
    for i in range(x-1,x+2):
        b = 0
        for j in range(y-1,y+2):
            arr[i][j] = arr2[a][b]
            b += 1
        a += 1

# (2)AAA체크함수
def AAA(array):
    ret = -1 # 불가능
    for i in range(N):
        for j in range(N-2):
            if arr[i][j:j+3] == ['A','A','A']:
                ret = 1 # 가능
                return ret
    return ret


position = []
for i in range(1,N-1):
    for j in range(1,N-1):
        position.append([i,j]) # N이 5이면, 총 9개좌표 -> 중복조합

answer = '불가능'
def dfs(start,level):
    global answer, arr
    if level >= 6:
        # answer = '불가능'
        return

    tmp = copy.deepcopy(arr)
    for i in range(len(position)):
        rotate(position[i][0],position[i][1])
        if AAA(arr) == 1:
            answer = '가능'
            return
        dfs(i,level+1) # i+1이 x
        arr = copy.deepcopy(tmp)


dfs(0,0)
print(answer)
# 답 자체는 나오는데.. VSC에서도 출력이 엄청 느리게 됨.. 음........이게 아닌가?