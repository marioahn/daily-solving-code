a = [[1,3],[2],[3,4]]

tmp = a[0] + a[2]
tmp.sort(reverse=True)
tmp = set(tmp)
print(tmp)