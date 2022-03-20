n = int(input())
arr = list(map(int,input().split()))
arr.sort() # 가벼운 순으로 꺼내져야 하므로
result = []
# 매번 2개씩 꺼내야하는데, 황금1 / 짱돌1 or 짱돌2 이렇게 남아있는 경우 break
# 꺼내는 기준: 가장 가벼운 돌!!
# 황금과 짱돌이 같은 무게일때는,황금이 먼저 나온다

while 1:
    if type(arr[0]) == str: # 처음 꺼내는 돌이 짱돌이면, 바로 break
        break
    elif type(arr[0]) != str and type(arr[1]) == str: # 두번째만 짱돌이면, 첫 황금은 추가해줘!
        result += [arr[0]]
        break
    elif type(arr[0]) != str and type(arr[1]) != str: # 둘다 황금이면,
        result += arr[0:2]
        tmp = arr[1]
        arr = arr[2:]
        # arr.append(tmp) # 어라. 이렇게 하면 짱돌인지 알 수가 없잖아. 심지어 무게 같은 황금이 있을땐 더더욱
        arr.append(str(tmp * 2)) # 짱돌은 str넣어서 구별!
        arr.sort(key=lambda i: int(i)) # ㅅㅂ 이렇게 하면되는구나

print(len(result))