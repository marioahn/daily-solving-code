# 처음 path는 0이될 수 없음
n = int(input())
numbers = list(map(int,input().split()))
used = [0] * n
path = []

min = 2e18
def abc(level):
    global path, min
    if level == 3:
        if path[0] == 0:
            return
        Sum = 0
        for i in range(3):
            Sum += path[i] * (10 ** (2-i))
        if min > Sum:
            min = Sum
        return

    for i in range(n):
        if used[i] == 0:
            path.append(numbers[i])
            used[i] = 1
            abc(level+1)
            path.pop() # 난 append했으니까 여기 필수
            used[i] = 0 # 여기 필수

abc(0)
print(min)