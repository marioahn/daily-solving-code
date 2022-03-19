# 훨씬 깔끔!
def link(arg):
    if arr[ord(arg)-65] == 0:
        return arg
    ret = link(arr[ord(arg)-65])
    arr[ord(arg) - 65] = ret # 여기 안 넣으면, C D -> A C -> A D가 arr= [0,0,'A','C']상태임 여전히.
    return ret

def union(a,b):
    la, lb = link(a),link(b)
    if la == lb:
        return 1 # 종료된다는 것 자체가, 이미 그룹이라는 뜻 ㅇㅇ.
    arr[ord(lb)-65] = la

n = int(input())
arr = [0]*4
ans = '미발견'
for i in range(n):
    y,x = input().split()
    if ans =='미발견' and union(y,x):
        ans = '발견'
print(ans)
print(arr)
# A C
# A B
# B D
# arr = [0,A,A,A]상태
# B C가 있어야, link(B) == link(C) == 'A'가 되면서 사이클이 완성되는 것ㅇㅇ
