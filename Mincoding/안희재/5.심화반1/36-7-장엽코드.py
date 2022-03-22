# 중복조합풀이! 난 조합으로 풀려고 했기에, 안되었던 것
cards = list(input())

path = ['']*4
cnt_odd = 0
cnt_even = 0
used = [0]*len(cards)
answer = []
def abc(level, start):
    if level == 4:
        if path[0] !=0:
            number = path[0]+path[1]+path[2]+path[3]
            answer.append(number)
        return

    for i in range(start, len(cards)):
        path[level] = cards[i]
        abc(level+1, i) # 중복조합이니까, i+1대신에 i..... ㅜ
        
abc(0, 0)


answer = [int(i) for i in answer]
for i in range(len(answer)):
    if answer[i] % 2 == 1:
        cnt_odd += 1
    else:
        cnt_even += 1


print(len(answer),end = ' ')
print(cnt_even, end=' ')
print(cnt_odd, end= ' ')