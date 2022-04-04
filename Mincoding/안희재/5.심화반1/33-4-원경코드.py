# 나와 달리 union find 제대로 사용했음! 굿
def link(x):
    try:
        x = int(x)
        if grade[x] == '':
            return x
        ret = link(grade[x])
        grade[x] = ret
        return ret
    except:
        return x

def union(a,b):
    la, lb = link(a),link(b)
    if la == lb:
        return
# 숫자+문자인 경우
    if type(lb) == str:
        grade[la] = lb
# 나머지 경우
    else:
        grade[lb] = la
# 숫자+숫자 또는 숫자+문자 또는 문자+숫자 형태로 정보가 들어옴
N, K = map(int, input().split())
info = [input().split() for _ in range(N)] # 정보
grade = ['']*(K+1) # 번호당 품목 적을 리스트
for i in range(N):
    union(info[i][0], info[i][1])
for i in range(1,K+1):
    if type(grade[i]) == int: # 값이 숫자인 경우, 등급으로 바꿔줌
        grade[i] = grade[grade[i]]
    print(grade[i],end='')