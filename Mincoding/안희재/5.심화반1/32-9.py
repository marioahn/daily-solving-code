word = list(input())
n = int(input())
word.sort(key=lambda x: ord(x[0]), reverse=True)
tmp = word[0:n]

stack = [[tmp[0],1]]
for i in range(1,len(tmp)):
    if tmp[i] != stack[-1][0]:
        stack.append([tmp[i],1]) # 딕셔너리처럼, 키와 값을 넣어줌!(리스트 형식으로)
    else:
        stack[-1][1] += 1

Max = 0
answer = ''
for i in range(len(stack)):
    if stack[i][1] > Max:
        Max = stack[i][1]
        answer = stack[i][0]

print(answer)

# 아 ......................... DAT사용하면 더 빨리 풀었을텐데............