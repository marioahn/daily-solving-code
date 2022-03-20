N = int(input())
arr = input().split()
arr.sort() # binary search는 항상 정렬시킨 후에 실행! - 알파벳 순, ++소문자는 몽땅 뒤로 가도록 정렬됨!

def abc(s, e, cnt):
    if s > e: # 아예 arr에 목록이 없음
        print('fail')
        return
    mid = (s+e) // 2
    if mid < title_idx:
        abc(mid+1,e, cnt+1)
    elif mid > title_idx:
        abc(s,mid-1, cnt+1)
    else:
        if cnt <= int(limit):
            print('pass')
            return
        else:
            print('fail')
            return

M = int(input())
for i in range(M):
    title, limit = input().split()
    if title in arr:
        title_idx = arr.index(title)
        abc(0,N-1,1) # 실수2: 처음에, N-1이 아니라 N으로 했었음..ㅠ idx찾는건데, len(arr)이 아니지..
    else:
        print('fail')
