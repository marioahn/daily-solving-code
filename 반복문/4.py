# -----------------------------------
# a, b = map(int,input().split())

# lst = ['T', 'B', 'T', 'S', 'A', 'K', 'L', 'I', 'Z', 'C']
# test_lst = lst[a:b+1] # (길이 b+1-a, 인덱스는 0부터 b-a까지)

# def move():
#     temp = test_lst[b-a]
#     for i in range(len(test_lst)-1, 0, -1):
#         test_lst[i] = test_lst[i-1]
#     test_lst[0] = temp

# # 2칸 이동
# move()
# move()

# # 아 근데, 다시 이식 시키는게 어렵네 어떻게 하는거지?
# lst[a:b+1] = test_lst[0:b+1-a] # 어 ㅋㅋ이게 되네 파이썬만..되나? 편하긴 하네
# # lst[a:b+1] = test_lst # 어라라 이것도 되넼
# print(lst)
# -----------------------------------
# 아, 근데 좀 더 범용적이려면 아래처럼, 더 직관적이기도 하네
arr=['T','B','T','S','A','K','L','I','Z','C']
index=list(map(int,input().split()))

def LMove(st,ed): # 이렇게 쓸 수 있는 이유 : 아래 줄에서 Lmove(index[0],index[1])
    temp=arr[st]
    for i in range(st,ed,1):
        arr[i]=arr[i+1]
    arr[ed]=temp

def RMove(st,ed):
    temp=arr[ed]
    for i in range(ed,st,-1):
        arr[i]=arr[i-1]
    arr[st]=temp


for i in range (2):
    LMove(index[0],index[1]) #여기가 핵심이네

print(*arr) #와; join안해도 되네

# 이렇게 하면 나처럼 test_list 따로 안만들어도 되는구나..
# 또한, 더 범용적이네 - 몇칸을 어느 방향으로 갈지 안 정해져있으면!