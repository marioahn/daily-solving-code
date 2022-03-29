# 조합문제
menu = [[500,30], [700,10], [600,30], [300,40], [400,20]] # [가격,포인트] 하드코딩
limit = int(input())
T = int(input()) # T는 종류

Max = 0

def dfs(start,level,sumPrice,sumPoint): # Sum은 가격들의 합
    global Max
    if level == T:
        amount = limit // sumPrice
        result =  sumPoint * amount
        Max = max(Max,result)
        return
    
    for i in range(start,len(menu)):
        dfs(i+1,level+1, sumPrice+menu[i][0], sumPoint+menu[i][1])

dfs(0,0,0,0)
print(Max)

