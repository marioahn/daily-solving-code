N = int(input()) # N * N
arr = [input() for _ in range(N)]
x, y = 0, 0

for i in range(N):
    if arr[i][0] == '0': # 최초로, '0'닿으면 직전꺼 담고 바로 break
        x = i-1
        break
else: # '#'가 끝까지 채워져있는 경우 ㅇㅇ.
    x = N-1

for i in range(N):
    if arr[x][i] == '0':
        y = i-1
        break

print(x,y)

# 아, 근데 이진탐색으로 풀어야 하네
# 34-2번풀었던것 처럼, 하면 될듯. ㅇㅇ. 전체적인 구조는 위와 같긴 함