# 조합문제, 단 used써야 중복입력된 한약 거를 수 있을듯?
# 아니 그냥.. 조합문제임.. ㅠ 아직도 개념 헷갈리네
# 아니구나, 중복조합문제네
    # 입력받는 문자중에서 중복된건 모두 제거하고,
    # 남은 것들끼리 중복조합 짜는 문제임
word = input()
result = []
for i in range(len(word)):
    if word[i] in result: continue
    result.append(word[i])
result.sort()

path = [''] * 3 
def dfs(start,level):
    if level == 3:
        print(*path,sep='')
        return

    for i in range(start,len(result)):
        path[level] = result[i]
        dfs(i,level+1) # i+1은 그냥 조합, i는 중복조합

dfs(0,0)



