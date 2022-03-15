# 문제: 0번 node에서 부터 DFS로 탐색하여Level 2에 도착할 때마다 경로를 출력
# 즉, 항상 0번노드부터 보면 되는 듯(0행)
n = int(input())
path = [0]
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def abc(level):
    if len(path) == 3:
        print(*path)
        return

    for i in range(n):
        if arr[level][i] == 1:
            path.append(i)
            tmp = i
            abc(tmp)
            path.pop() # 아 이거 꼭 넣어줘야 함 하;;;;

abc(0)

# path.pop().. 하;; 