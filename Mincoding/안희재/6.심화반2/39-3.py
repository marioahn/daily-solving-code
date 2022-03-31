n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x: x[1])

cnt = 1
standard = arr[0][1]
for i in range(1,len(arr)):
    if arr[i][0] >= standard:
        cnt += 1
        standard = arr[i][1]

print(cnt)