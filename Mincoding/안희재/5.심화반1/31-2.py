n = int(input())
arr = list(map(int,input().split()))

start = 0
end = 4
min = 2e18
while end <= n:
    if sum(arr[start:end]) < min:
        min = sum(arr[start:end])
    start += 1
    end += 1

print(min)
