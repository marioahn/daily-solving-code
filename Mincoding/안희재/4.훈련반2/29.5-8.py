# 아, 이게 아니지 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# dx,dy로 풀기..
arr = [['_','A','_'], ['#','_','D'], ['C','_','#'], ['#','_','_']]

# 1.right
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            if j+1 != 3 and arr[i][j+1] == '_':
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if arr[i][j] == 'C':
            if j+1 != 3 and arr[i][j+1] == '_':
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if arr[i][j] == 'D':
            if j+1 != 3 and arr[i][j+1] == '_':
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

# 2.down
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            if i+1 != 4 and arr[i+1][j] == '_':
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        if arr[i][j] == 'C':
            if i+1 != 4 and arr[i+1][j] == '_':
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        if arr[i][j] == 'D':
            if i+1 != 4 and arr[i+1][j] == '_':
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

# 3.left
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            if j-1 != -1 and arr[i][j-1] == '_':
                arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        if arr[i][j] == 'C':
            if j-1 != -1 and arr[i][j-1] == '_':
                arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        if arr[i][j] == 'D':
            if j-1 != -1 and arr[i][j-1] == '_':
                arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]

# 4.up
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            if i-1 != -1 and arr[i-1][j] == '_':
                arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
        if arr[i][j] == 'C':
            if i-1 != -1 and arr[i-1][j] == '_':
                arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
        if arr[i][j] == 'D':
            if i-1 != -1 and arr[i-1][j] == '_':
                arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]

# 5.left
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            if j+1 != 3 and arr[i][j+1] == '_':
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if arr[i][j] == 'C':
            if j+1 != 3 and arr[i][j+1] == '_':
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if arr[i][j] == 'D':
            if j+1 != 3 and arr[i][j+1] == '_':
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

for i in range(4):
    print(*arr[i],sep='')

