# 순열이긴 한데, 음..입력값에 같은 카드가 여러개 나올 수 있나? 그러면 36-7처럼 해야하는데
# 아니네 ㅎㅎ
card = input().split()
path = [''] * 4
used = [0] * 4

cnt = 0
def dfs(level):
    global cnt
    if level == 4:
        if int(''.join(path)) > 3129:
            cnt += 1
        return

    for i in range(4):
        if used[i] == 0:
            path[level] = card[i]
            used[i] = 1
            dfs(level+1)
            used[i] = 0

dfs(0)
print(cnt)