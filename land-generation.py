import json
import random

import numpy as np

import pygame


# Set the width and height of the screen [width, height]
mapWidth = 200
mapHeight = 200
size = (mapWidth, mapHeight)
screen = pygame.display.set_mode(size)
width = 20
height = 20
rowLen = int(mapWidth / width)
colLen = int(mapHeight / height)
margin = 2


def importData(file):
    # read file
    with open(file+'.json', 'r') as myfile:
        data = myfile.read()
    # parse file
    return json.loads(data)


landforms = importData('./data/landforms')


def printArray(arr):
    print('\n'.join([' | '.join([str(item['id']) for item in row])
                     for row in arr]))


def getSurroundingArrayItems(arr, arrRow, x, y):
    surroundingItems = []
    if(x > 0):
        surroundingItems.append(arrRow[x - 1])
    if(x < len(arrRow) - 2):
        surroundingItems.append(arrRow[x + 1])
    if(y > 0):
        surroundingItems.append(arr[y - 1][x])
    if(y < len(arr) - 2):
        surroundingItems.append(arr[y + 1][x])
    return surroundingItems


def randomLandform(bias=[]):
    biasedForms = landforms + (bias * 10)
    return biasedForms[random.randint(0, len(biasedForms) - 1)]


def landGen(arr, col):
    landRow = []
    for j in range(rowLen):
        bias = getSurroundingArrayItems(arr, landRow, j, col)
        landRow.append(randomLandform(bias))
    return landRow


landArray = []

for i in range(colLen):
    landArray.append(landGen(landArray, i))


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    font = pygame.font.Font('freesansbold.ttf', 12)

    # --- Drawing code should go here
    for col in range(colLen):
        for row in range(rowLen):
            text = font.render(str(col) + ':' + str(row), True, RED)
            # textRect = text.get_rect()
            # textRect.center = (20 * col - 10, 20 * row + 10, )
            # screen.blit(text, textRect)
            pygame.draw.rect(screen, landArray[row][col]['color'], pygame.Rect(
                20 * row, 20 * col,  width, height))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
