map = [[3,5,1], [3,8,1], [1,1,5]]

bitarray = [list(map(int,input().split())) for _ in range(2)]

print(bitarray)
# def masking(x,y):
#     sum = 0
#     for i in range(2):
#         for j in range(2):
#             if bitarray[i][j] == 1:
#                 sum += map[x+i][y+j]
#     return sum

# max = 0
# max_x, max_y = 0, 0
# for i in range(3):
#     for j in range(3):
#         if masking(i,j) > max:
#             max = masking(i,j)
#             max_x, max_y = i, j

# print(f'({i},{j})')
