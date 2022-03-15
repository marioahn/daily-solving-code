arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
# [3,5,9,10] / [2,6,9,11]
left = 0
right = 0 
result = []

while left < 4 and right < 4:
    if arr1[left] < arr2[right]:
        result.append(arr1[left])
        left += 1
    else:
        result.append(arr2[right])
        right += 1

    if left == 4:
        for i in range(right,4):
            result.append(arr2[i])
    if right == 4:
        for i in range(left,4):
            result.append(arr1[i])

print(*result)