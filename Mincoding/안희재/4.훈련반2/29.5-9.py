word1 = input()
word2 = input()
if len(word1) > len(word2):
    # word2를 기준으로
    long = len(word2)
    result = ''
    while 1:
        # 길이 2차이나면, 3개 탐색가능
        for j in range(len(word2)-long+1):
            for i in range(len(word1)-long+1):
                if word2[j:long+j] == word1[i:long+i]:
                    result = word2[j:long+j]
                    break
        if result != '':
            break
        long -= 1
else:
    long = len(word1)
    result = ''
    while 1:
        # 길이 2차이나면, 3개 탐색가능
        for j in range(len(word1)-long+1):
            for i in range(len(word2)-long+1):
                if word1[j:long+j] == word2[i:long+i]:
                    result = word1[j:long+j]
                    break
        if result != '':
            break
        long -= 1

print(result)

# abcde
# Aabc