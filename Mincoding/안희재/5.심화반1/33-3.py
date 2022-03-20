# 걍 입력받은 인접행렬 대각선으로 나눈후, 위쪽만 보고 선 그리면 될듯
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
bucket = [0] * n

def findboss(arg):
    if bucket[ord(arg)-65] == 0:
        return arg
    ret = findboss(bucket[ord(arg)-65])
    bucket[ord(arg)-65] = ret
    return ret

def union(a,b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    bucket[ord(fb)-65] = fa
    
answer = '미발견'
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i][j] == 1:
            x, y = chr(i+65), chr(j+65)
            if union(x,y) == 1:
                answer = 'cycle 발견'
                break
    if answer == 'cycle 발견':
        break

print(answer)
