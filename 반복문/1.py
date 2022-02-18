index = int(input())
lst = [3, 4, 1, 1, 2]

# 이거 인덱스가 몇이든 결과는 똑같잖아.. 1칸 이동이라
# 1번->2번으로, 2번값은 3번으로
new_lst = [lst[4]]
for i in range(len(lst)-1): #0~3 -> 1~4
    new_lst.append(lst[i])

print(new_lst)