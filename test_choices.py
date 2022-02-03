import random
wd = ("Δε", "Τρ", "Τε", "Πε", "Πα", "Σα", "Κυ")
we = [0, 1, 2, 1, 1, 2, 3]
mytraining = []
for _ in range(20):
    mytraining.extend(random.choices(wd, weights=we, k=10))
freq = {}
for i in mytraining:
    freq[i] = freq.get(i, 0) + 1
print(freq)

