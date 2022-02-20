arr = [[1,5,7], [4,8,2], [9,6,3]]

# 잘 봐봐. 가운데쪽은 가만히 있고, 외곽 숫자들만 이동하잖아
# 3*3 면, 2개씩 4개가 / 4*4면 3개씩 4개가.. 이런 식임

def move(array): # 한 바퀴 회전
    up = arr[0][0:2]
    right = [arr[0][2], arr[1][2]]
    down = arr[2][1:3]
    left = [arr[1][0], arr[2][0]]
    
    # step1
    arr[0][1] = up[0]
    arr[0][2] = up[1]
    # step2
    arr[1][2] = right[0]
    arr[2][2] = right[1]
    # step3
    arr[2][0] = down[0]
    arr[2][1] = down[1]
    #step4
    arr[0][0] = left[0]
    arr[1][0] = left[1]

move(arr)

print(arr)