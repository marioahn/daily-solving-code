cash = int(input())
coins = [10,50,100,500] # coins은 내림차순으로 sort

coins.sort(reverse=True)

idx = 0
cnt = 0
while cash != 0:
    cnt += cash // coins[idx]
    cash = cash % coins[idx]
    idx += 1

print(cnt)