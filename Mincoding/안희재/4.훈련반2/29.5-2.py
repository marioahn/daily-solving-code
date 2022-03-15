evid = [-1,0,0,1,2,4,4]
timeStamp = [8,3,5,6,8,9,10]

trace = int(input())

def abc(level):
    if evid[level] == -1:
        print('0번index(출발)')
        return

    tmp = evid[level]
    abc(tmp)
    print(f'{level}번index({timeStamp[level]}시)')

abc(trace)
