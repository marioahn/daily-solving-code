n = int(input())
arr = list(map(int,input().split()))

arr.sort()
Sum,cnt = 0,0
for i in range(len(arr)):
    Sum += arr[i]
    cnt += 1
    if Sum > 100:
        cnt -= 1
        break

print(cnt)

