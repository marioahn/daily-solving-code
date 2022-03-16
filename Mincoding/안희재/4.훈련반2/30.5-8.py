arr = ['B','I','A','H']
n = int(input())
cnt = 1
idx = 0
result = []

while 1:
    if len(arr) == 1:
        result.append(arr[0])
        break
    idx += 1
    cnt += 1
    if idx == len(arr):
        idx -= len(arr)
    if cnt == n:
        result.append(arr[idx])
        arr.pop(idx)
        cnt = 1
        
print(*result)