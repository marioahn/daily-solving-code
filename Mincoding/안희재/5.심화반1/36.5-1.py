word = input()

Max = 0
tmp = 0
for i in range(len(word)-1):
    if word[i] == '#':
        tmp = 0
    else:
        tmp += 1
        if word[i+1] == '#':
            if Max < tmp:
                Max = tmp

print(Max * '~')