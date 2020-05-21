# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []

for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        # if random.randint(0,1) == 0:
        if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main Program Loop
    print('\n\n\n\n\n') # Seperate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '') # Print the # or space.
        print() # Print a newline at the end of each row

    # Calculate the next step's cells based on the current steps cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the number of living neighbours:
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1 # Top-left neighbour is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1 # Top neighbour is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1 # Top-right neighbour is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1 # Left neighbour is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1 # Right neighbour is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1 # Bottom-left neighbour is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1 # Bottom neighbour is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1 # Bottom-right neighbour is alive.


            # Set cells based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells with 2 or 3 neighbours stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                # Dead cells with 3 neighbours become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering

