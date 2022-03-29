import copy
n = int(input())
arr = list(map(int,input().split()))

Max, path, result = 0, [], []
def dfs(Sum): # Sum도 전역변수보다는, 함수 인자로 넣기
    global Max, arr, result
    if sum(arr) == 0:
        if Max < Sum:
            Max = Sum
            result = []
            for i in range(len(path)):
                result.append(path[i])
        return

    tmp = copy.deepcopy(arr)
    for i in range(len(arr)):
        if arr[i] == 0: continue # 이렇게 교수님 방식으로 하자. 훨씬더 깔끔해 보임
        if i-1 >= 0 and i+1 < len(arr):
            arr[i-1], arr[i+1] = 0, 0
        elif i-1 < 0:
            arr[i+1] = 0
        else: # i+1가 범위벗어난 경우면
            arr[i-1] = 0
        point = arr[i]
        path.append(point)
        arr[i] = 0
        dfs(Sum+point)
        path.pop()
        arr = copy.deepcopy(tmp)

dfs(0)
result = list(map(str,result))
process = '+'.join(result)
print(f'{process}={Max}')