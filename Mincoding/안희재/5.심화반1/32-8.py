# title 함수쓰면 편하겠지만.. 일단 없이 해보자!
# --------------------------------------------
# 모두 소문자 -> title형식으로 -> !!!(1)번!!
# 모두 대문자 -> 그대로 -> (2)
# 대소문자 섞여있음
    # 근데, title형식 -> 그대로 -> (3)
    # 근본없이 섞여 -> 대문자 형식으로 -> !!(4)번!!
# 그니까, 바꿀 문자는 : 모두 소문자 or 근본없이 섞여있는 경우(대문자1개 and 첫글자가 대문자x + 대문자2개이상)
n = int(input())
words = [input() for _ in range(n)]

def changeStr(word, num):
    result = []
    if num == 1: # 1이면, 타이틀형식으로
        result.append(word[0].upper())
        for i in range(1,len(word)):
            result.append(word[i].lower())
    else: # num == 4면, 모두 대문자
        for i in range(len(word)):
            result.append(word[i].upper())
    
    return result

for i in range(len(words)):
    flag = 0
    for j in range(len(words[i])):
        if words[i][j].islower():
            flag += 1 # 소문자면 1씩, 대문자면 2씩 증가로 하자
        else: # 대문자라면,
            flag += 2

    if flag == len(words[i]):
        words[i] = ''.join(changeStr(words[i], 1))
    else:
        if len(words[i]) < flag < len(words[i]) * 2:
            if not(words[i][0].isupper() and flag == len(words[i]) + 1):
                words[i] = ''.join(changeStr(words[i],4))

words.sort(key=lambda x: ord(x[0]))
for i in range(n):
    print(words[i])