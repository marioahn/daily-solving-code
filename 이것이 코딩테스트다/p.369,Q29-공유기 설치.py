# 이진탐색
n,c = map(int,input().split())

house = []
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 좌표값의 최소값
start = 1
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start+end)//2 # 해당 gap
    old = house[0]
    count = 1 # 0번 인덱스에는 무조건 공유기 설치!

    for i in range(1, len(house)):
        if house[i] >= old+mid: # gap 이상
            count+=1
            old = house[i] # 여기에 공유기 설치!
    
    if count >=c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1 # start = mid - 1가 아님

print(result)

# 하.. 그냥 따라 치기만 했음.. 다시 처음부터 짜보기