def solution(n):
    people = 0
    total = 0
    while(True):
        total = people*(people-1)/2
        if n<total:
            break
        people+=1
    times = int(people-(total-n)-1)
    return [times,people]

# 엥? 내가 풀었던 코드 어디갔지..?
# 일단 답지로..