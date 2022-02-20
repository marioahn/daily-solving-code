arr = [['B','K','S','A','B'], ['T','B','T','S','T'], ['B','K','S','A','B'], ['T','T','B','S','C'], ['A','A','B','K','S']]
word = input()
# 단어는 일단 연속된 것
# 가로로만 검사
# 찾으면, 오른쪽으로 2회만 회전

def move(lst): # 우측 1칸 이동
    tmp = lst[len(lst)-1]
    for i in range(len(lst)-1,0,-1):
        lst[i] = lst[i-1]
    lst[0] = tmp

    return lst


for i in range(5): # 5행
    s = 0
    e = len(word) # 와따,, 이 조건들 밖에다 넣으면 한번밖에 안 돌아가지 반복문이..
    while e <= 5: # word가 bks, 3이면 딱 3번만. j= 0,1,2 // =까지 붙여야지, s:e는 e는 포함x니까
        if ''.join(arr[i][s:e]) == word:
            arr[i][s:e] = move(arr[i][s:e])
            arr[i][s:e] = move(arr[i][s:e])
        else:
            s += 1
            e += 1

print(arr)