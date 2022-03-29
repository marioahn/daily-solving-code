# ...난.. 쥬륵..
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    dir = [0]*(N+1)
    dir[0] = -1

    def group(a,b):
    
        while(True):
            if dir[a] == 0:
                break
            else:
                a = dir[a]

        while(True):
                if dir[b] == 0 or dir[b] == a:
                    dir[b] = a
                    break
                else:
                    t = dir[b] # tmp
                    dir[b] = a
                    b = t

    for i in range(M):
        a,b=arr[2*i],arr[2*i+1]
        if a > b:
            a,b = b,a
        group(a,b)

    print(f'#{tc} {dir.count(0)}')