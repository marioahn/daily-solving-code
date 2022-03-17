arr = [list(map(int,input())) for _ in range(5)]
line1, line2 = map(int,input().split())

for end in range(1, len(arr[line1])):
    i = end
    while i > 0 and arr[line1][i - 1] > arr[line1][i]:
        arr[line1][i - 1], arr[line1][i] = arr[line1][i], arr[line1][i - 1]
        i -= 1

for end in range(1, len(arr[line2])):
    i = end
    while i > 0 and arr[line2][i - 1] > arr[line2][i]:
        arr[line2][i - 1], arr[line2][i] = arr[line2][i], arr[line2][i - 1]
        i -= 1

for i in range(5):
    print(arr[i][0],end= ' ')

# 삽입정렬로 바로바로!