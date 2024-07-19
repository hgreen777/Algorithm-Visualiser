#Imports 
import time
import pygame
import Algorithms
import random

"""Constants and initialisation of pygame """
screenX = 400
screenY = 600
running = True
arraySize = 400

pygame.init()
screen = pygame.display.set_mode((screenX,screenY))     #Useable 500, 400
pygame.display.set_caption("Algorithm Visualiser")
clock = pygame.time.Clock()

"""ARRAY CREATION & HANDLING"""
def createArray(size):
    arr = []
    for i in range(1,size + 1):
        arr.append(i)
    
    return arr

def shuffleArray(arr):
    """Uses Fisher-Yates to shuffle array"""
    #https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    
    n = len(arr)

    for i in range(0, n-2):
        j = random.randint(i, n)
        arr[i], arr[j] = arr[j], arr[i]

"""UPDATING VISUALS"""
def dimensionConstantSet(arr, x,y):
    '''Updates the constant dimensions used to draw the square arrays.
       Used when the array size changes.                                '''
    global height_interval, width
    # Semi Constants For Box Dimenstions
    height_interval = y / len(arr)
    width = x / len(arr)

    # BEWARE IF VARIABLE, CONSTANTS MAY NOT PRODUCE INTEGERS, POTENTIALLY BREAKING SYSTEM
    
def updateVisual(arr):
    '''Updates the visual based of an array at a given point.'''
    for index, item in enumerate(arr):
        # Calculatre variable dimensions
        height = item * height_interval
        left = index * width
        top = screenY - height

        # Cretae rect & draw to screen
        dimensions = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, "White", dimensions)

a = createArray(arraySize)
dimensionConstantSet(a, screenX, screenY)

"""GAME LOOP"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    updateVisual(a)

    pygame.display.flip()

    clock.tick(5)    

pygame.quit()