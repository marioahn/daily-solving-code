arr = [list(map(int,input().split())) for _ in range(3)]
Gop = 1
for i in range(3):
    Sum = 0
    for j in range(3):
        Sum += arr[j][i]
    Gop *= Sum

print(Gop)