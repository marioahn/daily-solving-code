# 일단, 한번쓴건 다시 못씀
# 첫 번째 줄에 5개의, 10미만 자연수가 주어집니다.
# 어;; 근데 used 평범하게 사용하면 안될것 같은데;; 5 4 3 / 5 3 4 같..은거잖아.. 5 4 3 vs 9 4 5..? 
# 이 문제는 "조합"인데, 어떻게 보여주지?
# 그래서 결국 마지막에 n!로 나눠줘서 풀긴했음
num = list(map(int,input().split()))

def abc(level, amount):
    global cnt
    if level == amount:
        if sum(path) < 10 or sum(path) > 20:
            return
        cnt += 1
        return
    for i in range(5):
        if used[i] == 0:
            path[level] = num[i]
            used[i] = 1
            abc(level+1, amount)
            used[i] = 0 # 이거 여기서는 꼭 써줘야함

def factorial(a):
    result = 1
    for i in range(1,a+1):
        result *= i
    return result

Sum = 0
for n in range(2,6):
    cnt = 0
    path = [0] * n # n= 2~5 / 10미만이므로, n=1일때 10~20 충족 못함
    used = [0] * 5
    abc(0,n)
    Sum += (cnt // factorial(n))

print(Sum)
