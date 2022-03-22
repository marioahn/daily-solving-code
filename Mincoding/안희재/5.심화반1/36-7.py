cards = input() # index봐야하니까, 문자형으로
path = [0] * 4
used = [0] * 6 # 중복x, 순열 / 단, 처음은 0 xx
# 근데, 또 최종결과는 한번씩만 세어줘야함 - 마지막은 조합처럼..? how??
# 난 일단 야매쓴다 ㅠ
    # result에 중복x순열들을 모두 담는데,
    # 마지막 level에서 result순회 후, 이미 있는거면 추가 안하도록 코드 작성(야매 조합..?)
    # 다른 방법이 있나?
result = [0]

cnt, odd, even = 0, 0, 0
def abc(level):
    global cnt, odd, even
    if level == 4:
        for i in range(len(result)): # 맨 처음의 경우 에러나니까 result에 0초깃값 채워줌 ㅇ;;
            if result[i] == ''.join(path):
                # 처음에 그냥 path리스트를 통째로 넣어서, result 2중배열 되었는데,
                # 이중배열 얕은복사 문제 생겨버려서 위처럼 했음
                break
        else: # 끝까지 다 돌았는데, 없으면 새로 추가
            result.append(''.join(path))
        return

    for i in range(6):
        if level == 0 and int(cards[i]) == 0:
            continue
        if used[i] == 0:
            path[level] = cards[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0

abc(0)
cnt = len(result)-1 # 첨에 0이라는 의미없는 초기값 넣었으므로
for i in range(1,len(result)):
    if int(result[i][-1]) % 2:
        odd += 1
    else:
        even += 1
print(cnt, even, odd)