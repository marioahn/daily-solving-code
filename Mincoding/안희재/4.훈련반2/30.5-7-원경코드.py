def five(level=0,total=0):
    global cnt
    if total > 20:
        return
    if level == 5:
        if 10 <= total <= 20:
            cnt +=1
        return
    for i in range(2): # i = 0, 1 -> 쓸지 / 말지
        used[level] = 1*i 
        five(level+1,total+arr[level]*i)

arr = list(map(int, input().split()))
cnt = 0
used = [0]*5
five()
print(cnt)

# 와;; 조합은 이렇게 풀어야지 내 코드는 쓋;;;
