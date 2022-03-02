# 3 3 3 2 1 1
# 3 3 3 2 2 1
# 3 3 3 3 3 2
# 2 2 3 2 2 2
# 2 2 3 2 2 2
# 2 2 2 2 2 2
N, X = map(int,input().split())
arr = list(map(int,input().split()))
stack = [0] * N

# 각 순회하면서 stack에 쌓기
def validate(): # 변수 뭐로?
    answer = ''
    for i in range(len(arr)):
        if abs(arr[i] - stack[-1]) > 1: # 직전칸과 높이가 2차이나면 바로 컷
            answer = 0
            return
        else:
            stack[i] = arr[i] # 아니라면, 일단 추가해줌

    # 다시 arr순회하면서 stack검사
    for i in range(len(arr)):