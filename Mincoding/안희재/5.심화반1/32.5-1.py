arr = ['ABCD','ABCE','AGEH','EIEI','FEQE','ABAD']
word = input()

for i in range(4):
    for j in range(6):
        if word[i] != '?':
            if word[i] != arr[j][i]:
                arr[j] = '0000' # len(0)은 오류뜨므로, '0'으로 하면 인덱스오류 뜸-> '0000'!!

cnt = 0
for i in range(len(arr)):
    if arr[i][0] != '0':
        cnt += 1

print(cnt)