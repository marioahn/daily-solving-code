meat = list(input())

def flip(x): # 뒤집기 함수 - 너무 노가다인데.. 좀 줄일 수 없나?
    if x-1 >= 0 and x+1 < len(meat):
        if meat[x-1] == 'O':
            meat[x-1] = 'X'
        else: meat[x-1] = 'O'
        if meat[x+1] == 'O':
            meat[x+1] = 'X'
        else: meat[x+1] = 'O'
    elif x-1 >= 0:
        if meat[x-1] == 'O':
            meat[x-1] = 'X'
        else: meat[x-1] = 'O'
    else:
        if meat[x+1] == 'O':
            meat[x+1] = 'X'
        else: meat[x+1] = 'O'
    if meat[x] == 'O':
        meat[x] = 'X'
    else: meat[x] = 'O'

flip(1)
print(meat)