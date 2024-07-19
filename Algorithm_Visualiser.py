#Imports 
import time
import pygame
from Algorithms import bubbleSort
import Algorithms
import random

"""TODO"""
# TODO : Allow the algorithm to be stoped prematurely (and subsequently allow exiting of program) - Button (start/stop button) 
# TODO : Count & Show Comparisons. 
# TODO : Allow user to control array size & frame-rate with drop down menu - (see dropdown in E/Programming)
# TODO : Add algorithms and allow user to change the current algorithm.
# TODO : Polish The implementation
# TODO : Add music ...

"""Constants initialisations"""
screenX,useableX = 800, 800
screenY = 600
useableY = screenY - 50
running = True
array_size = 100

"""PYGAME initialisations"""
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
    n -= 1

    for i in range(0, n-1):
        j = random.randint(i, n)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

"""UPDATING VISUALS"""
def dimensionConstantSet(arr, x,y):
    '''Updates the constant dimensions used to draw the square arrays.
       Used when the array size changes.                                '''
    global height_interval, width
    # Semi Constants For Box Dimenstions
    height_interval = y / len(arr)
    width = x / len(arr)

    # BEWARE IF VARIABLE, CONSTANTS MAY NOT PRODUCE INTEGERS, POTENTIALLY BREAKING SYSTEM
    
def updateVisual(arr, selected):
    screen.fill("Black")    # Resets screen

    '''Updates the visual based of an array at a given point.'''
    for index, item in enumerate(arr):
        # Calculatre variable dimensions
        height = item * height_interval
        left = index * width
        top = screenY - height

        colour = "White"
        if index == selected:
            colour = "Red"

        # Cretae rect & draw to screen
        dimensions = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, colour, dimensions)
    
    pygame.display.flip()
    clock.tick(120)


"""Setting up for Game Loop"""
# Creating & Shuffling array to be used by sorting algorithm.
a = createArray(array_size)
a = shuffleArray(a)
dimensionConstantSet(a, useableX, useableY)


"""GAME LOOP"""
sorting_started = False

def quitCheck():
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if not sorting_started:    
        bubbleSort(a, updateVisual, quitCheck)
        sorting_started = False

    pygame.display.flip()   

pygame.quit()