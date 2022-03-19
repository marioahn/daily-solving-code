n = int(input())
arr = [input().split() for _ in range(n)]
tmp = [arr[i][0] for i in range(len(arr))] # 입력 순서만 기억하는 배열
result = [arr[0]]
print(result[0][0]) # 처음껀 정렬필요없으니까 일단 출력하고 보자
# result = sorted(tmp,key=lambda x: int(x[1]),reverse=True) 

for i in range(1,n):
    result.append(arr[i]) # 입력 순대로, 차근차근 result에 추가시켜가면서 정렬도 동시에 하는 반복문!
    # step1: 점수순으로 배열
    result = sorted(result,key=lambda x: int(x[1]),reverse=True) 
    # step2: 이제 점수가 같은 것들은, 순서상 나중에 온게 앞으로 오도록!(index함수 이용)
    for j in range(len(result)-1):
        if result[j][1] == result[j+1][1]: # 점수는 같고,
            if tmp.index(result[j][0]) < tmp.index(result[j+1][0]): # 입력순이 나중이라면,
                result[j], result[j+1] = result[j+1], result[j] # 앞으로 와!
    final = [result[i][0] for i in range(len(result))]
    print(*final[0:3])

# 아오;; 쉬운 문제였는데 왜 도대체 이걸..


