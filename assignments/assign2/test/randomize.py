import random

items = open('LotsOfWords.txt').read().splitlines() 

file = open('LotsOfWordsRandom.txt', 'a+')

while len(items) > 0:
    # Get random item
    i = random.choice(items)
    # get index of item
    dex = items.index(i)
    del items[dex]
    file.write(f'{i}\n')
    print(f'Wrote element: {i}')



file.close()