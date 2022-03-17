n = int(input())
arr = input().split()

cnt = 0
for i in range(n-1):
    for j in range(i,n):
        if arr[i]+arr[j] == 'HITSMUSIC':
            cnt += 1

print(cnt)