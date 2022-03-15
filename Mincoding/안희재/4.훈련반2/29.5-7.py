idx, life = map(int,input().split())

while 1:
    if life == 0 or idx ==5:
        print('_____')
        break
    lst = ['_'] * 5
    lst[idx] = life
    print(*lst,sep='')
    life -= 1
    idx += 1
