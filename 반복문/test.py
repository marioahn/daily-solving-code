a = ['B','K','S','A','B']
word = input()

def move(lst): # 우측 1칸 이동
    tmp = lst[len(lst)-1]
    for i in range(len(lst)-1,0,-1):
        lst[i] = lst[i-1]
    lst[0] = tmp

    return lst


s = 0
e = len(word)

while e < 5: # word가 bks, 3이면 딱 3번만. j= 0,1,2
    if ''.join(a[s:e]) == word:
        a[s:e] = move(a[s:e])
        a[s:e] = move(a[s:e])
    else:
        s += 1
        e += 1

print(a)