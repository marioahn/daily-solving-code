alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
path = [''] * 4
def abc(level,str):
    global cnt
    if level == 4:
        cnt += 1
        if path == str:
            print(cnt)
        return

    for i in range(26):
        path[level] = alphabet[i]
        abc(level+1,str)


n = int(input())
for i in range(n):
    cnt = 0
    password = list(input())
    abc(0,password) 