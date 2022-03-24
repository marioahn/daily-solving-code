word = list(input())

answer = []
sum = 0
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        answer.append(word[i])
    else:
        sum += int(word[i])

answer.sort()
answer.append(str(sum))
print(''.join(answer))

