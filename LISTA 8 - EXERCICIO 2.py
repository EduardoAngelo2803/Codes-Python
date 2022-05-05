ordem = []
frase = str(input())


for i in frase:
    ordem.append(i)
    
ordem.sort(reverse=True)

count_chars = {}
for char in ordem:
    if char not in count_chars:
        count_chars[char] = 0
    count_chars[char] += 1


for i, v in count_chars.items():
    print(i, v)
  
