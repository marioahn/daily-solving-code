arr = list(map(int,input().split()))

bucket = [0] * 10 # μ«μ 0~9λκΉ

for i in range(len(arr)):
    idx = arr[i]
    bucket[idx] += 1

result = []

for i in range(len(bucket)):
    if bucket[i] != 0:
        for j in range(bucket[i]):
            result.append(i)

print(*result)