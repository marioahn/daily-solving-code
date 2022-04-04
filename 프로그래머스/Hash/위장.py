clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    answer = 1
    hash = {}
    for i in range(len(clothes)):
        if not clothes[i][1] in hash:
            hash[clothes[i][1]] = 1
        else:
            hash[clothes[i][1]] += 1
            
    for value in hash.values():
        answer *= (value+1)
        
    return answer-1

# 아.. 걍 단순한 수학문제였네 ㅠ 4,3,2개로 총 3종류 있으면,
# (4+1)*(3+1)*(2+1)-1 하면 됨..(+1한 경우는 0개 고를 때)
# 및, 마지막에 1빼주는 경우는 모-든 경우에서 3종류 모두 0개 고를 경우(최소 1가지는 집어야 하니까)