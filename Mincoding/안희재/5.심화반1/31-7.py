n = int(input())
arr = [input() for _ in range(n)]

for i in range(n-2):
    for j in range(n-1-i):
        if len(arr[j]) > len(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
        if len(arr[j]) == len(arr[j+1]):
            idx = 0
            while 1:
                if ord(arr[j][idx]) > ord(arr[j+1][idx]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    break
                elif ord(arr[j][idx]) == ord(arr[j+1][idx]):
                    idx += 1
                else:
                    break # 현상유지하고 다음 for문으로 ㄱㄱ, 이거 꼭 있어야 함!

for i in range(len(arr)):
    print(arr[i])