N = int(input())
arr = list(map(int,input().split()))
arr.sort()

result = 0 # 그룹 수
cnt = 0 # 현재 그룹의 구성원 수
for ele in arr:
    cnt += 1
    if cnt >= ele:
        result += 1
        cnt = 0 # 그룹 1개 완성시켰으니, 구성원 수는 초기화

print(result)
