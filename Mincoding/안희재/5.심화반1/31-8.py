P = int(input())
N = int(input())
result = []

# 4715 x 2 = 9430 --> 349 : 이 경우만 주의
for i in range(N):
    P = str(2*P)[::-1]
    if P[0] == '0':
        P = P[1:]
    P = int(P)

print(P)