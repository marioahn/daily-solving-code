n, x = map(int,input().split())
arr = list(map(int,input().split()))

# 1.x의 첫 인덱스, result1 찾기
s = 0
e = len(arr)-1
result1 = -1
while s <= e:
    mid1 = (s+e) // 2
    if arr[mid1] > x:
        e = mid1 - 1
    elif arr[mid1] == x:
        if mid1-1 < 0:
            result1 = mid1 # x = 1, 1 1 2 2 2 3 3의 경우
            break
        elif arr[mid1-1] != x:
            result1 = mid1
            break
        else:
            e = mid1 - 1
    else:  # arr[mid1] < x인 경우
        if arr[mid1+1] == x:
            result1 = mid1+1
            break
        else:
            s = mid1 + 1

# 2.x의 마지막 인덱스 찾기
s2 = 0
e2 = len(arr)-1
result2 = -1
while s2 <= e2:
    mid2 = (s2+e2) // 2
    if arr[mid2] > x:
        if arr[mid2-1] == x:
            result2 = mid2-1
            break
        else:
            e2 = mid2 - 1
    elif arr[mid2] == x:
        if mid2+1 == len(arr): # x=3, 1 1 2 2 2 2 3의 경우 : mid2+1은 없지. 
            result2 = mid2
            break
        elif arr[mid2+1] != x:
            result2 = mid2
            break
        else:
            s2 = mid2 + 1
    else: # arr[mid2] < x인 경우
        s2 = mid2 + 1

if result1+result2 < 0: # 두개다 -1에서 안 바뀜 = 찾는데 없었다
    print(-1)
else:
    print(result2-result1+1)

# 독하다 독해 아 구현 왜이리 까다롭지
# 그냥 이진탐색이 안 익숙해서 그런것 같기도 하고..
# 다뤄야 할 조건이 좀 여러개라서 그런것 같기도 하고...