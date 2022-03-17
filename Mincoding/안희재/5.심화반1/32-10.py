# 1순위 : 빈도수
# 카운트가 같으면, 그제야 숫자 작은 순

n = int(input()) 
arr_n = [list(map(int,input().split())) for _ in range(n)]
arr_b = [list(map(int,input().split())) for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if arr_b[i][j] == 1:
            result.append(arr_n[i][j])

# 음.. 버킷만들면 오히러 더 복잡해질것 같은데,, 그냥 딕셔너리처럼 하는게 나을듯
    # [[cnt, 숫자] ... []]
result.sort() # 일단 정렬은 시켜둬야지 # 2 4 4 7
stack = [[1, result[0]]]
for i in range(1,len(result)):
    if result[i] != stack[-1][1]:
        stack.append([1,result[i]])
    else:
        stack[-1][0] += 1

stack.sort(key=lambda x: x[0], reverse=True) # 음..sort함수가 x[0]가 같으면, x[1]도 알아서 정렬해주네
answer = []
for i in range(len(stack)):
    answer += [stack[i][1]] * stack[i][0]

print(*answer)