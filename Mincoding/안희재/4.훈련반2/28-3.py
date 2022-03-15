arr = [
    [0,1,1,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

word = input()
idx = 0
family = ['A','B','C','D','E','F','G','H']
for i in range(len(family)):
    if family[i] == word:
        idx = i

# boss = 0 # 아. 이거 이렇게만 두면, 형제 없는 경우 잘못 출력된다
boss = -1
for i in range(len(family)):
    if arr[i][idx] == 1:
        boss = i
if boss != -1:
    for i in range(len(family)):
        if arr[boss][i] == 1 and i != idx:
            print(family[i], end= ' ')
else:
    print('없음')