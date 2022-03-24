N = int(input())
arr = [input() for _ in range(N)]

# 0.중복조합문제 - 최대6번까지만 가능. level 6번 넘어가면 return
    # 중간에 가로 AAA가 발견되면 바로 answer = '가능'으로 바꾸고 return
# 1.테두리는 불가능 -> 일단 선택가능한 좌표부터 구해야지

# 3*3의 테두리를 회전시키는 함수
def rotate(x,y): # x,y를 중심으로 테두리 회전(3*3배열)
    directx = [-1,-1,-1,0,0,1,1,1] # 위에서부터 가로탐색 -> 내려오기
    directy = [-1,0,1,-1,1,-1,0,1]
    

position = []
for i in range(1,N-1):
    for j in range(1,N-1):
        position.append([i,j]) # N이 5이면, 총 9개좌표




