arr = list(map(int,input().split()))
arr.sort()
Sum = 0
for i in range(len(arr)-1):
    Sum += arr[i]*(3-i)

print(Sum)
