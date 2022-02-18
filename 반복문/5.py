# 어.. 그냥move한번 더 하면 되는거 아닌가?
# N=2이면 move()총 4번 돌리고..?
# ------------------------------
# N = int(input())
# lst = [3, -1, 1, -1, 2, -1, 8, -1, 9]

# def move():
#     temp = lst[len(lst)-1]
#     for i in range(len(lst)-1, 0, -1):
#         lst[i] = lst[i-1]
#     lst[0] = temp

# for j in range(N):
#     move()
#     move()

# print(lst)
# --------------------------------
# 아 안되는구나. 마지막 -1경우 총 3번을 움직여야 돌아가서 어긋남
# ㅎㅎ;; 야매 컷!
N = int(input())

lst = [3, -1, 1, -1, 2, -1, 8, -1, 9]

def move2():
    temp = lst[len(lst)-1]
    for i in range(len(lst)-1, 0, -2):
        lst[i] = lst[i-2]
    lst[0] = temp

for i in range(N):
    move2()

print(lst)