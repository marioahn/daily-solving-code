# 각 문자는 한번만 사용가능하지
# 조합이용해서 풀기!!!!! - 교수님 say
import copy
word = list(input())
idx = [0,1,2,3,4]
n = int(input())
path = [''] * len(word)


def art(list):
    Sum = 0
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            Sum -= 50
        if 0 < abs(ord(list[i]) - ord(list[i+1])) <= 5:
            Sum += 3
        if abs(ord(list[i]) - ord(list[i+1])) >= 20:
            Sum += 10
    return Sum

Max = -2e18
def abc(level):
    global Max, word
    if level == n:
        if Max < art(word):
            Max = art(word)
        return

    used = [0] * len(word)
    backup = copy.deepcopy(word)
    for i in range(len(word)):
        used[i] = 1
        for j in range(len(word)):
            if used[j] == 0:
                word[i], word[j] = word[j], word[i]
                abc(level+1)
                word = backup
        used[i] = 0
        

abc(0)
print(Max)
