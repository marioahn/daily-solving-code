n = int(input())
arr = [0] * 4

def findboss(arg):
    if arr[(ord(arg)-65)] == 0:
        return arg
    ret = findboss(arr[(ord(arg)-65)])
    return ret

def union(a,b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[ord(fb)-65] = fa

answer = '미발견'
for i in range(n):
    x, y = input().split()
    if union(x,y) == 1:
        answer = '발견'
        break

print(answer)