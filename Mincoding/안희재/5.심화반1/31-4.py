string = [list(input()) for _ in range(5)]

for i in range(5):
    string[i][1], string[i][3] = string[i][3], string[i][1]

for i in range(5):
    if ''.join(string[i]) == 'MAPOM':
        print('yes')
        break
else:
    print('no')
