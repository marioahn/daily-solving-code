# 이 문제 아이디어 싸움임
# 누구는 몇줄안에 끝나고 누구는 몇십줄..
# 진짜 좋은 문제라고 하심!

# 음;; 피보나치처럼..?
n = int(input()) # n단
accu = [0] * (n+1) # 1번인덱스에 1단을 두기 위해 n+1
accu[1], accu[2] = 1, 2 # 피보나치처럼 초기값

for i in range(3,n+1):
    accu[i] = accu[i-1] + accu[i-2]

print(accu[n])
