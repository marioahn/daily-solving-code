n = int(input())
start, end = 1, 1
for i in range(n):
    a, b = input().split()
    if b == 'DOWN':
        end = int(a)-1
    else:
        start = int(a)+1

if start > end:
    print('ERROR')
elif start == end:
    print(start)
else:
    print(f'{start} ~ {end}')