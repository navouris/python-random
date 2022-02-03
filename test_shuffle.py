import random
cards = []
values = ['c', 'd', 'h', 's',  ]
for _ in range(1,11):
    cards.extend([str(_)+x for x in values])
for f in ['J', 'Q', 'K']:
    cards.extend([f+x for x in values])
print(cards)
random.shuffle(cards)
print(cards)