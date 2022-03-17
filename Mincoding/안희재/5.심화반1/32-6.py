candidate, voters = map(int,input().split())
arr = [[] for _ in range(candidate)] # arr = [[] * candidate] ㄴㄴ deepcopy문제
for i in range(voters):
    vote = input().split()
    if vote[0] == '0':
        arr[0] += [vote[1]]
    elif vote[0] == '1':
        arr[1] += [vote[1]]
    elif vote[0] == '2':
        arr[2] += [vote[1]]
    elif vote[0] == '3':
        arr[3] += [vote[1]]
    else:
        arr[4] += [vote[1]]

result = []
Max, idx = 0, 0
for i in range(len(arr)):
    if len(arr[i]) > Max:
        Max = len(arr[i])
        idx = i

print(*arr[idx])