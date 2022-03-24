import copy
string = list(input())
slen = len(string)
n = int(input())
Max = -1

def calculation(string):
    global slen
    score = 0
    for i in range(slen):
        now = string[i]
        if 0 <= i+1 < slen:
            beside = string[i+1]
            if now == beside:
                score -= 50
            elif abs(ord(now)-ord(beside)) <= 5:
                score += 3
            elif abs(ord(now)-ord(beside)) >= 20:
                score += 10
    return score
    
def dfs(start, cnt):
    global n, string, Max, slen
    if cnt == n:
        res = calculation(string)
        Max = max(Max, res)
        return
    backup= copy.deepcopy(string)
    for i in range(start, slen): # 01 02 03 04 비교후 12 13 14 비교후 23 24 비교후 34 -> (3번 과 4번 index값 비교한다는 뜻)
        for j in range(i+1, slen):
            string[i], string[j] = string[j], string[i] # swap
            dfs(i+1, cnt+1)
            string = copy.deepcopy(backup) # 원상복구
dfs(0, 0)
print(Max)