# 흠.. 걍 여태했던 move함수에, 마지막 경우 (2,0), (1,0), (1,1)만 좀 다르게?
arr = [[1,2,3], [4,5,6], [7,8,9]]

def move():
    arr2 = [[0] * 3 for _ in range(3)]
    # 북쪽
    for i in range(2):
        arr2[0][i+1] = arr[0][i]
    # 동쪽
    for i in range(2):
        arr2[i+1][2] = arr[i][2]
    # 남쪽
    for i in range(2):
        arr2[2][i] = arr[2][i+1]
    # 서쪽
    for i in range(2):
        arr2[1][i] = arr[2-i][0]
        #arr2[1][0], arr2[1,1] = arr[2][0], arr[1][0]
    # 가운데 0,0으로 보내기
    arr2[0][0] = arr[1][1]

    return arr2

print(move())