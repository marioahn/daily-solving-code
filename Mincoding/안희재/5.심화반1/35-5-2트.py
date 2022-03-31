import heapq

n = int(input())
index = list(map(int,input().split()))
ugly = [1]

p2 = p3 = p5 = 0
while len(ugly) <= max(index):