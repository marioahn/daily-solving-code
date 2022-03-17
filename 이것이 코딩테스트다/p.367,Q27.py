n, x = map(int,input().split())
arr = list(map(int,input().split()))
result = arr.count(x)
if result == 0:
    print(-1)
else:
    print(result)
# ㄴㄴ; 시간복잡도(logN) 문제임.. -> 선형탐색으로 불가능
# 이진탐색 써야 함