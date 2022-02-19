N, M, K = map(int,input().split()) # N은 사람 수, M초에 K개를 만들 수 있음
times = list(map(int,input().split()))

# 일단, 도착하는 사람들의 시간 sort로 정렬
times.sort()

# times 첫 손님이 일단 M보다 작으면 무조건 impossible
for i in range(len(times)):

