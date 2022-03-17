n = int(input())
lst = [list(input().split()) for _ in range(n)]
lst.sort(key=lambda x: ord(x[1]))

for i in range(n-1):
    for j in range(n-1-i):
        if lst[j][0] > lst[j+1][0]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(n):
    print(*lst[i])

# 5 A
# 1 C
# 5 E
# 4 F
# 5 F
# 4 T
# 1차 정렬한 결과 -> 알파벳 순 정렬이 되었으므로,
# 이제 전체 버블소트로 숫자만 바꿔주면 됨!
# 숫자먼저 정렬하고, 알파벳순으로 하려면 은근히 골치아파서 이렇게 했음.