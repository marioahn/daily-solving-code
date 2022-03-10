num = input() # 걍 문자로 불러오기
num_list = [num[i] for i in range(len(num))]
num_list = list(map(int,num_list)) # 숫자화
middle = len(num) // 2

back_arr = num_list[:middle]
front_arr = num_list[middle:]

if sum(back_arr) == sum(front_arr):
    print('LUCKY')
else:
    print('READY')