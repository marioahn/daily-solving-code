# 일단, 2부터 N-1까지의 소수를 담은 배열을 구한 후에. INDEX 0에서부터 한개씩 늘려나가는 식
# 근데, 시간초과..
n = int(input())

prime = []
check = [0] * (n+1)

for i in range(2,n+1):
    if check[i] == 0: prime.append(i)
    for j in range(i+i,n+1,i):
        check[j] = 1

cnt, start = 0, 0
while 1:
    if start >= len(prime): break

    Sum = 0
    for i in range(start,len(prime)):
        Sum += prime[i]
        if Sum == n:
            cnt += 1
            start += 1
            break
        elif Sum > n:
            start += 12
            break
    else: # for else문
        start += 1

print(cnt)

