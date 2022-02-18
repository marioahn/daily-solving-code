# ------------------------------
# N = int(input())
# lst = [9, 3, 5, 7, 4]
# bucket = lst * 2

# print(bucket[5-N:10-N])
# ------------------------------
# N = 1이면 : bucket[4:9]
# N = 2이면 : bucket[3,8]
# 이렇게 풀었는데 반복문으로 풀라고 문제에 나와있어서 다시 품
N = int(input())
lst = [9, 3, 5, 7, 4]

def Move():
    temp = lst[4]
    for i in range(4, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = temp

for j in range(N):
    Move()

print(lst)
