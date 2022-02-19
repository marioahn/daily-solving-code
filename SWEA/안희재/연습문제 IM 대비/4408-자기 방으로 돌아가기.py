T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = []
    for i in range(N):
        room = list(map(int,input().split()))
        arr.append(room)
        # 이중 리스트 완성

    arr.sort() # 이중 리스트, 각 요소는 2개의 요소를 가짐(현재, 돌아갈 방)
    # sort하면 0번인덱스 우선 -> 같으면 1번 인덱스 비교해서 정렬해줌(이중 리스트라도)

    # 0번친구의 고향이 1번친구의 시작점보다 작아야 동시에 가능함
    # 아니면, cnt + 1
    # arr[0][1] vs arr[1][0] / arr[1][1] vs arr[2][0] / arr[2][1] vs arr[3][0]
    cnt = 1 # 디폴트값은 0이 아닌, 1
    for i in range(len(arr)-1):
        if arr[i][1] >= arr[i+1][0]: # =도 써줘야
            cnt += 1

    print(f'#{tc}', cnt)