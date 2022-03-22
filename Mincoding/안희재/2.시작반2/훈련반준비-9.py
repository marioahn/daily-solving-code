arr = []
for i in range(2):
    num = list(map(int,input().split()))
    arr.append(num)

arr2 = []
for i in range(2):
    for j in range(3):
        arr2.append(arr[i][j])

arr2.sort()
tmp = 0
for i in range(2):
    for j in range(3):
        arr[i][j] = arr2[tmp]
        tmp += 1

for i in range(2):
    print(*arr[i])

# 문제 이상한데 뭐;; 억지로 풀면 아래처럼!
# ----------------------------------------
# how = input().split()
# if len(how) == 3:
#     arr = [list(map(int, x)) for x in [how,input().split()]]
#     lst = [arr[i//3][i%3] for i in range(6)]
# else:
#     lst = list(map(int, how))
# for i in range(5):
#     for j in range(i+1,6):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(*lst[:3])
# print(*lst[3:])
# ----------------------------------------