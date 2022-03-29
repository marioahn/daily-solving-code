# 나는 filp함수 썼는데, 딕셔너리로 간단하게 했음 ;; ㄷㄷ 굿
def roast(arg=0):
    global min_turn,meat
    if arg == 4:
        return
    if meat == ['O']*number or meat == ['X']*number:
        if min_turn > arg:
            min_turn = arg
            return
    for i in range(number):
        backup = meat[:]
        for j in range(-1,2):
            if 0 <= i+j < number:
                meat[i+j] = after[meat[i+j]]
        roast(arg+1)
        meat = backup[:]

meat = list(map(str,input()))
number = len(meat)
after = {'O':'X', 'X':'O'} # 요렇게!
min_turn = 5
roast()
if min_turn == 5:
    print('impossible')
else:
    print(min_turn)