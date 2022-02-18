N = int(input())
lst = ['A', 'T', 'B', 'T', 'S']

def plus_Move():
    temp = lst[4]
    for i in range(4, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = temp

def minus_Move():
    temp = lst[0]
    for j in range(0, 4):
        lst[j] = lst[j+1]
    lst[4] = temp

for k in range(abs(N)):
    if N < 0:
        minus_Move()
    else:
        plus_Move()

print(lst)