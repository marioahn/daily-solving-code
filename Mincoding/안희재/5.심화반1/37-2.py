original = list(input())
n = int(input())
arr = [15,20,44,22,55,16,45]
    # a,b,c,d,e,f,g / ord('a') = 97

# 6개 중에서, 2개 제외면 6개중에서 4개뽑는 조합!
# 아. 총6개 합에서 n개를 빼는 식으로 해도 될듯?

Max = 0
def dfs(level, start, remains):
    global Max
    if level == n:
        if remains % 10 == 0 and Max < remains:
            Max = remains
        return

    for i in range(start,len(original)):
        dfs(level+1, i+1, remains-arr[ord(original[i])-97])

Sum = 0
for i in range(len(original)):
    Sum += arr[ord(original[i])-97]
dfs(0,0,Sum)
print(Max)