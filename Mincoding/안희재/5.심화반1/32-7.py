n = int(input()) # 입력 좌표 수
arr = [[] for _ in range(n)]
for i in range(n):
    x, y, crops = input().split()
    # 근데,, 딱히 좌표가 필요한가..?
    for j in range(len(crops)):
        arr[i] += [int(crops[j])]

winds = int(input())
powers = list(map(int,input().split()))

for i in range(winds):
    for j in range(n):
        if len(arr[j]) != 0:
            if powers[i] > arr[j][-1]:
                arr[j].pop()
            else:
                arr[j][-1] -= powers[i]
                if arr[j][-1] == 0:
                    arr[j].pop() # 0은 바로 빼버려야지

Sum = 0
for i in range(n):
    Sum += len(arr[i])
print(Sum)