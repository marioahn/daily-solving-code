genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	
hash = {}
for i in range(len(genres)):
    hash[genres[i]] = plays[i]

print(hash)
