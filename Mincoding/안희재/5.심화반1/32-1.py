n = int(input())
lst = [list(input().split()) for _ in range(n)]
lst.sort(key=lambda x: int(x[0]))
for i in range(n-1):
    if lst[i][0] == lst[i+1][0]:
        if ord(lst[i][1]) > ord(lst[i+1][1]):
            lst[i], lst[i+1] = lst[i+1], lst[i]

for i in range(n):
    print(*lst[i])

# 아. 이렇게 해도 미완성임.
# 1 C
# 4 T
# 4 F
# 5 E
# 5 F
# 5 A
# -> 처음 정렬하면 이렇게 되는데,
# 알파벳 순 정렬이 한번씩만 됨. 할거면 버블소트하든지 해야지..
# 그니까, 같은 숫자가 3개이상인 경우 꼬이게 되는 것!


# lst.sort(key=lambda x: int(x[0]))
# lst.sort(key=lambda x: ord(x[1]))
# 이렇게 쓰면 처음 정렬이 다시 엉키게 됨;;
