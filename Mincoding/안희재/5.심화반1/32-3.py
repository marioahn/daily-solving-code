n = int(input())
arr = list(map(int,input().split()))
# 아 그냥 sliding window??
stack = []

s, e = 0, 3
while 1:
    if arr[s] == arr[s+1] == arr[s+2]:
        stack.append([s,e])
        s += 3
        e += 3
    else: # 아니면 +1씩만!
        s += 1
        e += 1
    if e >= len(arr):
        break
# stack : [[3, 6], [8, 11], [11, 14]]
result = []
a, b = 0, stack[0][0]
result += arr[a:b]
for i in range(len(stack)-1):
    a, b = stack[i][1], stack[i+1][0]
    result += arr[a:b]
result += arr[stack[-1][1]:]

result.sort()
print(*result)

# 걍 연속된 3개가 보일때마다, 그 인덱스 tmp에 계속 담아두고
# tmp 포문돌리면서, 그 인덱스를 arr에서 빼면 될듯
# [[3, 6], [4, 7], [5, 8], [8, 11], [11, 14], [12, 15]]
# 첨엔 for문으로 range(len(word)-2)로 했는데 위 처럼 뜸. 
# 연속된3개 체크할때마다 건너 뛰어야 하므로 while로 체인지

# 22
# 1 1 1 1 1 1 1 1 1 2 3 3 3 3 2 2 2 2 2 3 1 2
# 아 이 경우 안되네 ㅋㅋㅋㅋㅋㅋㅋ 처음에 조건을,
# if sum(arr[s:e]) == tmp * 3:로 했는데,
# stack = [[0, 3], [3, 6], [6, 9], [10, 13], [14, 17], [18, 21]]
# 2,3,1인경우 ㅋㅋㅋㅋㅋ가 추가되네 ㅋㅋㅋㅋㅋ