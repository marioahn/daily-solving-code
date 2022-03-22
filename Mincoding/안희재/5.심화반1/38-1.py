# 와 근데, 이 문제 dfs일거라고는 생각 잘 못할것 같은데;;
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
# 일단, 순열(날짜 앞으로만 가니까)

Max = 0
def dfs(start,Sum):
    global Max
    if start >= n:
        if Max < Sum:
            Max = Sum
        return

    for i in range(start,n):
        dfs(i+arr[i][0], Sum+arr[i][1])

for i in range(len(arr)):
    dfs(i+arr[i][0],arr[i][1])

print(Max)

# 5
# 2 20
# 2 30
# 1 5
# 2 10
# 1 30