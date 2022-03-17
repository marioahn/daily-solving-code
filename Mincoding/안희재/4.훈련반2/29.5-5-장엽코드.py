arr = [list(map(int, input().split())) for _ in range(4)]

result = []
for i in range(len(arr)):
    for k in range(len(arr[i])):
        if arr[i][k] == 1:
            result.append([i,k])

print('({},{})'.format(result[0][0], result[0][1]))
print('({},{})'.format(result[-1][0], result[-1][1]))

# 와.........................