word = list(input())

print(*word,sep='')
while 1:
    for i in range(len(word)):
        if word[i] != '_':
            word[i] = chr(ord(word[i])-1)
            if word[i] == '@':
                word[i] = '_'
    print(*word,sep='')
    if word.count('_') == len(word):
        break