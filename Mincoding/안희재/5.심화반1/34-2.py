arr = list(input())

def binary(s, e):
    if s > e:
        return #인데, 최소 1칸은 차있다고 하니까 사실상 필요 없음
    
    mid = (s+e) // 2
    if arr[mid] == '#':
        if arr[mid+1] == '_':
            print(f'{(mid+1)*10}%')
            return
        else:
            binary(mid+1,e)
    else: # '_'면
        if arr[mid-1] == '#':
            print(f'{(mid-1)*10}%')
        else:
            binary(s,mid-1)


binary(0,len(arr))