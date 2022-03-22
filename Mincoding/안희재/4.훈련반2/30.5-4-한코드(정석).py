a = list(input())
b = list(input())
c = list(input())
def abc(m, n):
    if len(m) > len(n):
        return m
    elif len(n) > len(m):
        return n
    else:
        for i in range(len(n)):
            if m[i] != n[i]:
                if m[i] == '1':
                    return m
                else:
                    return n
d, e = abc(a, b), abc(b, c)
ans = abc(d, e)
for i in range(len(ans)):
    print(ans[i], end="")