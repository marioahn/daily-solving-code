N = int(input())
arr = list(map(int,input().split()))
arr.sort() # 그리디 문제는 일단 정렬시키고 봐야!
# 1 2 2 2 3 
# 음. 그냥 앞에서부터 그룹 만들면 될것 같은데..?
cnt = 0
start = 0
end = 0
while 1:
    flag = 0
    end += arr[start]
    if len(arr[start:end]) >= arr[start]: # 1 2 2 2 2 2 2 3의 경우도 고려해야.
        for i in range(start,end):
            if arr[i] > arr[start]:
                flag = 1
                break
    else:
        break
    if flag == 1:
        break
    cnt += 1
    start = end

print(cnt)

# 앞에서부터 그룹을 만드는 것은 맞았지만, 더 간단하게 구현할 수 있었다 ㅠ