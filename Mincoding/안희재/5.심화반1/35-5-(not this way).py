# heap문제 -> 어.. heap으로 어케풀지..?

n = int(input())
index = list(map(int,input().split()))
ugly = [1]

p2 = p3 = p5 = 0
while len(ugly) <= max(index):
    tmp2 = ugly[p2] * 2
    tmp3 = ugly[p3] * 3
    tmp5 = ugly[p5] * 5
    if min(tmp2,tmp3,tmp5) == tmp2:
        if tmp2 == tmp3 == tmp5: # (1)3개 다 같은 경우도 해줘야 함;
            p2, p3, p5 = p2+1, p3+1, p5+1
            ugly.append(tmp2)
        elif tmp2 == tmp3: # (2)
            p2, p3 = p2+1, p3+1
            ugly.append(tmp2)
        elif tmp2 == tmp5:
            p2, p5 = p2+1, p5+1 # (3)
            ugly.append(tmp2)
        else:
            p2 += 1
            ugly.append(tmp2)
    elif min(tmp2,tmp3,tmp5) == tmp3:
        if tmp3 == tmp5: # (4)
            p3, p5 = p3+1, p5+1
            ugly.append(tmp3)
        else:
            p3 += 1
            ugly.append(tmp3)
    else:
        p5 += 1
        ugly.append(tmp5)

# print(ugly)
for i in range(len(index)):
    print(ugly[index[i]-1], end= ' ')