max = 0
result = ''

for i in range(3):
    word = input()
    sum = 0
    for i in range(1,len(word)+1):
        sum += (2**(i-1)) * int(word[-i])
    if max < sum:
        max = sum
        result = word

print(result)