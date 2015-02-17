import random
numhands = 4
for c in range(1, numhands):
    c = [r+s for r in '2345789TJQKA' for s in 'SHDC']

for x in range(1, numhands):
    random.shuffle(x)
