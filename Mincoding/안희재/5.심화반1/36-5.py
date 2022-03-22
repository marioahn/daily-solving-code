word = input()
words = ['BTS','SBS','BS','CBS','SES']

Min = 2e18
def abc(level, remains):
    global Min
    if len(remains) == 0:
        if level < Min:
            Min = level

    for i in range(5):
        if remains[0:len(words[i])] == words[i]:
            abc(level+1, remains[len(words[i]):])

abc(0,word)
print(Min)