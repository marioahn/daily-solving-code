a = list(input())
b = list(input())
c, d = ['']*len(a), ['']*len(a)
rst, maxx = 0, 0
def abc(A, B):
    global a, b, c, d, rst, maxx
    if A >= len(a) or B >= len(b):
        if rst > maxx:
            maxx = rst
            for x in range(len(a)):
                d[x] = c[x]
        return
    if a[A] == b[B]:
        rst += 1
        c[A] = a[A]
        abc(A+1, B+1)
        rst -= 1
        c[A] = ''
    else:
        if rst > maxx:
            maxx = rst
            for x in range(len(a)):
                d[x] = c[x]
        if rst > 0:
            return
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    abc(i, j)
abc(0, 0)
for i in range(len(a)):
    if d[i] != '':
        print(d[i], end="")