import random
numberOfStreaks = 0
flips = []
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    flips.append(random.randint(0,1)) 

    # Code that checks if there is a streak of 6 heads or tails in a row
currentFlip = None
numOfFlips = 0
for flip in flips:
    if flip == currentFlip:
        numOfFlips += 1
        if numOfFlips == 6:
            numberOfStreaks += 1
    else:
        numOfFlips = 0
        currentFlip = flip


print('Chance of streak: %s%%' % (numberOfStreaks/100))