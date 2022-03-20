N, K = map(int,input().split())
arr = [0] * K

tmp = []
for i in range(N):
    x, y = input().split()
    if ord(x) <= 57 and ord(y) <= 57: # (3, 2)
        if arr[int(x)-1] == 0 and arr[int(y)-1] == 0: # 둘다 없으면, 왼쪽에 있는 걸로 채우기(x)
            arr[int(x)-1], arr[int(y)-1] = x, x
        elif arr[int(x)-1] == 0 and arr[int(y)-1] != 0: # 한쪽만 채워져있으면 나머지도 그걸로 채우기
            arr[int(x)-1] = arr[int(y)-1]
        elif arr[int(x)-1] != 0 and arr[int(y)-1] == 0:
            arr[int(y)-1] = arr[int(x)-1]
        else: # 둘 다 이미 채워져있으면? pass 사이클이니까 아무 의미없음 ㅇㅇ.
            continue
    elif ord(x) <= 57: # (1, A)
        if arr[int(x)-1] == 0:
            arr[int(x)-1] = y
        else:
            tmp = arr[int(x)-1]
            for i in range(len(arr)):
                if arr[i] == tmp:
                    arr[i] = y
    else: # (A, 1)
        if arr[int(y)-1] == 0:
            arr[int(y)-1] = x
        else:
            tmp = arr[int(y)-1]
            for i in range(len(arr)):
                if arr[i] == tmp:
                    arr[i] = x

print(*arr,sep='')
