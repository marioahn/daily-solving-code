avoidable = ['chicken', 'pizza', 'jockbal', 'bread', 'samhap']
word = input()

s = 0 # start
tmp = 0
answer = ''
while 1:
    for i in range(5):
        if word[s:s+len(avoidable[i])].lower() == avoidable[i]:
            answer += word[tmp:s] + '###'
            s += len(avoidable[i])
            tmp = s
            break
    else:
        s += 1

    if s > len(word):
        break

print(answer)