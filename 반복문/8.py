arr = [6,9,2,0,4,6,7,1,9,3]

s1, e1, s2, e2 = map(int,input().split())

def r_move(lst): # 우측회전
    tmp = lst[len(lst)-1]
    for i in range(len(lst)-1,0,-1):
        lst[i] = lst[i-1]
    lst[0] = tmp

arr1 = arr[s1:e1+1]
arr2 = arr[s2:e2+1]

r_move(arr1)
r_move(arr1)
r_move(arr2)
r_move(arr2)

arr[s1:e1+1] = arr1
arr[s2:e2+1] = arr2

print(arr)