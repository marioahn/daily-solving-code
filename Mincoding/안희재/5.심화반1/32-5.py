n = int(input())
arr = [input() for _ in range(n)]

Max_length = len(max(arr))
# 걍 전부 사전순으로 배열해놓고, 마지막에 길이순서로 정렬하는게 편할듯
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        for k in range(Max_length):
            if k == len(arr[j]): # bhc, bhc경우 ㅠ 여기 추가해줘야 인덱스오류 안뜸
                break
            if ord(arr[j][k]) > ord(arr[j+1][k]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                break # 한번 위치바뀌면 바로 break!
            elif ord(arr[j][k]) < ord(arr[j+1][k]):
                break # 이 경우도 꼭 써줘야 함. 안 그러면, 위에 바뀔때까지 or 끝까지 진행됨
            else: # 같은 경우는, 다음 경우로 pass. 이렇게 총 3가지 써줘야 제대로 작동함!
                continue

# step2: 길이순 배열(최종)
arr.sort(key=lambda x: len(x))

for i in range(n):
    print(arr[i])