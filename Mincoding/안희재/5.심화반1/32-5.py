n = int(input())
arr = [input() for _ in range(n)]

# step1 : 길이 짧은 순으로 정렬
arr.sort(key=lambda x: len(x))
s, e = 0
while 1:
    if len(arr[s]) == len(arr[e]):
        e += 1
