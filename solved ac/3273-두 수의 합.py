# ------------------ 처음 풀이 - 시간 초과로 실패
# cnt = 0
# for i in range(n-1):
#     for j in range(i+1,n):
#         sum = arr[i] + arr[j]
#         if sum != x:
#             continue
#         else:
#             cnt +=1
#             break
    
# print(cnt)
# ------------------
# 시간복잡도 제한 O(n)인듯
# 서로 다른 n개의 정수라고 했음
# 아. 정렬해서 투포인터로 풀면 될듯..

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()
# [1,2,3,5,7,9,10,11,12]

s = 0
e = len(arr)-1
sum = 0
cnt = 0
while s < e:
    sum = arr[s]+arr[e]
    if sum == x:
        cnt+=1 
        s += 1
        e -= 1
    elif sum > x:
        e -= 1
    else: # sum < x
        s += 1

print(cnt)

