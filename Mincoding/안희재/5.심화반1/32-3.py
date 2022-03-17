n = int(input())
arr = list(map(int,input().split()))
# 아 그냥 sliding window??
s = 0
e = 3
result = []
stack = []

for i in range(n):
    if len(stack) == 0:
        result.append(arr[i])
        stack.append(arr[i])
    elif 0 < len(stack) < 3:
        if arr[i] != stack[0]:
            stack = [] # 초기화
            result.append(arr[i])
            stack.append(arr[i])
        else: # 같으면?
            result.append(arr[i])
            stack.append(arr[i])
    else: #if len(stack) == 3:
        for i in range(3):
            result.pop()
            stack.pop()
            
print(result)