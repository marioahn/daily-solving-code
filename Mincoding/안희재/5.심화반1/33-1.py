n = int(input())
edge = []
for _ in range(n):
    edge.append(input().split())

arr=[0]*200

def findboss(member):
    global arr
    if arr[ord(member)]==0:
        return member
    ret=findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

def union(a,b):
    global arr
    fa,fb=findboss(a),findboss(b)
    if fa==fb:
        return 1 # 여기 추가
    arr[ord(fb)]=fa

# for i in range(n):
#     union(edge[i][0], edge[i][1]) 
# 여기 빼니까 되네 비로서;;; 아오;;;; 여길 왜 넣누.. 여기 넣으면 이미 arr = [0,A,A,A]가 되어서
# 아래 코드에서 첫장부터 바로 ret==1이되어서 break. 즉, 무조~건 "발견"
answer = "미발견"
for i in range(n):
    a, b = edge[i]
    ret = union(a, b)
    if ret==1:
        answer = "발견"
        break
print(answer)
print(arr)