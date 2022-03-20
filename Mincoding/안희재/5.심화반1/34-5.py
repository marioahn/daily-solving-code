# binary search 이용
n = int(input())
arr = [i for i in range(1,n+1)]
target = n ** (1/2)
s, e = 0, len(arr)-1
while 1:
    mid = (s+e) // 2
    if arr[mid] > target:
        if arr[mid-1] < target:
            print(arr[mid-1])
            break
        else:
            e = mid-1
    elif arr[mid] < target:
        if arr[mid+1] > target:
            print(arr[mid])
            break
        else:
            s = mid+1
    else:
        print(mid)
        break


