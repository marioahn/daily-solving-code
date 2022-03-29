# rotate나보다 훨씬 간단;;;;
from copy import deepcopy
def rot(y,x,num=1):
    global puzzle
    result = deepcopy(puzzle)
    if num:
        for i in range(-1,2):
            for j in range(-1,2):
                puzzle[y+j][x-i] = result[y+i][x+j]
    else:
        for i in range(-1,2):
            for j in range(-1,2):
                puzzle[y+i][x+j] = result[y+j][x-i]

def solve(arg=0):
    global puzzle,possible
    if arg == 6:
        return
    for i in range(N):
        for j in range(N-2):
            if puzzle[i][j] == 'A':
                if puzzle[i][j+1:j+3] == ['A']*2:
                    possible = 1
                    return
    for i in range(1,N-1):
        for j in range(1,N-1):
            # backup = deepcopy(puzzle)
            rot(i,j)
            solve(arg+1)
            rot(i,j,0)
            # puzzle = deepcopy(backup)

N = int(input())
puzzle = [list(map(str,input())) for _ in range(N)]
possible = 0
solve()
if possible:
    print('가능')
else:
    print('불가능')