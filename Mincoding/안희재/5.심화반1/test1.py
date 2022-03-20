arr = [3, '1', 4, '2']

arr.sort(key=lambda i: int(i))
print(arr)

# word.sort(key=lambda x: ord(x[0]), reverse=True)