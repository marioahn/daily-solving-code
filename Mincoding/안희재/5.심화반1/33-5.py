N = int(input())
arr = list(map(int,input().split()))
acts = int(input())
bucket = [0] * N
for i in range(acts):
    act, x, y = input().split()
    if act == 'alliance':
        if bucket[ord(x)-65] == 0 and bucket[ord(y)-65] == 0:
            bucket[ord(x)-65], bucket[ord(y)-65] = x, x
        elif bucket[ord(x)-65] != 0 and bucket[ord(y)-65] == 0:
            bucket[ord(y)-65] = bucket[ord(x)-65]
        elif bucket[ord(y)-65] != 0 and bucket[ord(x)-65] == 0:
            bucket[ord(x)-65] = bucket[ord(y)-65]
        else:
            continue
    else: # act == 'war'
        tmp1, tmp2, sum1, sum2 = bucket[ord(x)-65], bucket[ord(y)-65], 0, 0
        for i in range(len(bucket)):
            if bucket[i] == tmp1:
                sum1 += arr[i]
            if bucket[i] == tmp2:
                sum2 += arr[i]
        if sum1 > sum2: # x집단이 이기면, y집단 버킷은 -1로
            for i in range(len(bucket)):
                if bucket[i] == tmp2:
                    bucket[i] = -1
        else: # y집단이 이기면, x집단 버킷은 -1
            for i in range(len(bucket)):
                if bucket[i] == tmp1:
                    bucket[i] = -1

# bucket -> ['A', -1, 'A', -1, 0, 'A', 0]
cnt = 0
for i in range(len(bucket)):
    if type(bucket[i]) == str or bucket[i] >= 0:
        cnt += 1

print(cnt)