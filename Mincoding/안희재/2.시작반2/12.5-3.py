arr = [['D','A','D'],['Q','W','Q'],['A','S','D'],['A','S','D']]

def main():
    word = input()
    return word

def find(x):
    result = '์์'
    for i in range(4):
        for j in range(3):
            if arr[i][j] == x:
                result = '์กด์ฌ'
                print(result)
                return
    print(result)
    return

find(main())