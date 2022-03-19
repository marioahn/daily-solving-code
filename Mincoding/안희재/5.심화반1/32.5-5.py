arr = [3,2,-1,3,-2,0,-1] # 0은 테러범 위치
n = int(input())

def abc(level):
    if arr[level] == 0:
        print('5번')
        return
    
    abc(level+arr[level])
    print(f'{level}번')

abc(n)