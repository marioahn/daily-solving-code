arr = [4,4,5,7,8,10,20,22,23,24]
n = int(input())

def abc(s, e): # s, e를 인자로
    if s > e:
        print('X')
        return
    mid = (s+e) // 2
    if arr[mid] < n:
        abc(mid+1,e)
    elif arr[mid] > n:
        abc(s,mid-1)
    else: # arr[mid] == n:
        print('O')
        return

abc(0,len(arr)) # s, e