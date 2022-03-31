# 투포인터 사용해보자 이번엔
# 엥??? 이것도 시간초과네??
# 에라토스테네스의 체 구현이 문제인가?
    # ㅇㅇ;;;; 에라토스테네스에서, 두 번째 포문을 밖에다 넣으면 시간이 훨씬 더 걸리겠지
    # 에라토스테네스 쓰는 의미가 퇴색됨!!
n = int(input())

prime = []
check = [0] * (n+1)

for i in range(2,n+1):
    if check[i] == 0:
        prime.append(i)
        for j in range(i+i,n+1,i):
            check[j] = 1

cnt, start, end = 0, 0, 1
while 1:
    if end > len(prime): break

    tmp = sum(prime[start:end])
    if tmp == n:
        cnt += 1
        end += 1
    elif tmp < n:
        end += 1
    else: # tmp > n
        start += 1

print(cnt)