import random
r = []
for _ in range(1000):
    r.append(random.random())
freq = {}
for i in r:
    for j in [i/10 for i in range(11)]:
        if i <= j: 
            freq[j] = freq.get(j, 0) + 1
            break
print(freq)
print( sum([freq[x] for x in freq.keys()]))