import copy

food = list(map(int,input().split())) # 길이는 항상 6
times = int(input())
# 1번독수리: 0~2번인덱스 / 3번: 1~4번 / 2번: 3~5번
# used사용 필수, 순열!(1번독수리->3번->2번독수리)
# 1~3번 or 1~4번 or 3~5번만 카드를 선택 가능
# 그리고 매번 남은 먹이는 2배 
# 어라; 그냥 times횟수만큼 재귀 abc(0)을 돌리고, level은 3개 고르니까 3개로 해..?브랜치는 각3,3,4로 하고..
# used, path사용할 필요 없음
Max = 0
def abc(level,Sum):
    global Max, food
    if level == times:
        if Max < Sum:
            Max = Sum
        return
    if level > 0:
        food = list(map(lambda x: x * 2, food)) # for문보단 람다로!

    tmp = copy.deepcopy(food)
    small = 0 # 변수 한개 더 만들기 - 이번 횟수에 먹은 먹이들
    for i in range(0,3): # 0~2
        for j in range(1,5): # 1~4
            for k in range(3,6): # 3~6
                small += food[i]
                food[i] = 0
                small += food[j]
                food[j] = 0
                small += food[k]
                food[k] = 0
                abc(level+1,Sum+small)
                food = copy.deepcopy(tmp) # food = tmp 이게 ㄴㄴ
                small = 0 # 다시 초기화 첫 for문이 아닌, 여기 마지막에서 초기화를 시켜줘야 함
                # small += (food[i]+food[j]+food[k]) 
                # food[i],food[j],food[k] = 0,0,0 0
                # abc(level+1,Sum+small)
                # food = copy.deepcopy(tmp)
                # small = 0 
                # 위처럼 하면 안되는 이유: idx가 같고 비어있지 않다면, 그 먹이를 2배 더해주게 됨 - 물리적으로 불가!
                # 따라서, 순차적으로 코드를 적어야 됨..
abc(0,0)
print(Max)

# 처음 했던 코드 ---
# for i in range(3): # 0~2
#     Sum += food[i]
#     food[i] = 0
#     for j in range(1,5): # 1~4
#         Sum += food[j]
#         food[j] = 0
#         for k in range(3,6): # 3~6
#             Sum += food[k]
#             food[k] = 0
#             abc(level+1)
#             food = copy.deepcopy(tmp) # food = tmp 이게 ㄴㄴ
#             Sum -= food[k] # 이미 food[k] = 0 인데 어떻게 뺌 ㅠㅠ
#         Sum -= food[j]
#     Sum -= food[i]
