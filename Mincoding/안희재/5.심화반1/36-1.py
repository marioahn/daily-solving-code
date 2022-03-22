# 아 조합이구나;; - 같은 재료를 넣어도 되지만, 같은 결과는 xx!
# AAB -> ABA ㄴㄴ 
# 아니 근데, 같은 재료를 넣어도 된다는 조건때문에 좀 어려운데;;?
# 이거 조합이 아니라 조합 응용인것 같네..? = "중복조합"

word_list = list(input())
path = [''] * 3

def abc(level, start):
    if level == 3:
        print(*path,sep='')
        return 

    for i in range(start,len(word_list)):
        path[level] = word_list[i]
        abc(level+1, i)
        

abc(0, 0)


