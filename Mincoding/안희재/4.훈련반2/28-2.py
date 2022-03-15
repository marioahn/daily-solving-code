n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        arr[i][j] = row[j]

boss = 0
for i in range(n):
    if arr[i][0] == 1: # 현수는 0번노드이므로, 열이 0인게 현수꺼.
        boss = i

under = []
for i in range(n):
    if arr[0][i] == 1:
        under.append(i)

under_re = ''
for i in range(len(under)):
    under_re += str(under[i]) + ' '

print(f'boss:{boss}') # 직속 보스는 1명이라 괜찮은데, 부하가 문제네..
print(f'under:{under_re}')
