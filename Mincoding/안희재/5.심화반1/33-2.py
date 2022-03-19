     # A  B  C   D  E   F  G  H  I  J
arr = [0,'A','A',0,'D','D',0,'G',0,'I']

def findboss(arg):
    if arr[ord(arg)-65] == 0:
        return arg
    ret = findboss(arr[ord(arg)-65])
    arr[ord(arg)-65] = ret
    return ret

def union(a,b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[ord(fb)-65] = fa

n = int(input())
for i in range(n):
    x, y = input().split()
    union(x,y)

print(f'{arr.count(0)}개')