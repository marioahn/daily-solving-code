lst1 = list(input())

lst2 = ['S', 'E', 'Y', 'U', 'I', 'O', 'Q', 'X', 'D', 'E']

# 인덱스 찾아야 하나? 하아~ 음;; 다른 방법 있지 않을까?
# 일단, 인덱스는 여기에서 찾아야지,,, 처음에 move()한 후에 찾아버렸음;;
start_index = lst2.index(lst1[0])

def move():
    temp = lst1[len(lst1)-1]
    for i in range(len(lst1)-1, 0, -1):
        lst1[i] = lst1[i-1]
    lst1[0] = temp

move()
move()

lst2[start_index:start_index+len(lst1)] = lst1
result = ' '.join(lst2)

print(result)