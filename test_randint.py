import random
r = []
for _ in range(1000):
    r.append(random.randint(1,100))
freq = {}
for i in r:
    for j in [i for i in range(10, 101, 10)]:
        if i <= j: 
            freq[j] = freq.get(j, 0) + 1
            break
print(freq)
print( sum([freq[x] for x in freq.keys()]))