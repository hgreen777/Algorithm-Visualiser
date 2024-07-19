#Imports 
import time
import pygame
from Algorithms import bubbleSort
import Algorithms
import random
import math

"""TODO"""
# TODO : Allow user to control array size & frame-rate with drop down menu - (see dropdown in E/Programming)
# TODO : Add algorithms and allow user to change the current algorithm.
# TODO : Polish The implementation
# TODO : Add music ...

"""Constants initialisations"""
screenX,useableX = 800, 800
screenY = 600
useableY = screenY - 50
running = True
array_size = 200
play_btn_center = (30,30)
play_btn_radius = 25
txt_location = (play_btn_center[0] + play_btn_radius + 20, play_btn_center[1] - 15)
framerate = 5000

"""PYGAME initialisations"""
pygame.init()
screen = pygame.display.set_mode((screenX,screenY))     #Useable 500, 400
pygame.display.set_caption("Algorithm Visualiser")
txt_font = pygame.font.Font(None, 40)
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
# STATIC VISUALS
def staticVisuals():
    # Play Button
    global play_btn
    play_btn = pygame.draw.circle(screen, "Green",play_btn_center, play_btn_radius)


# DYNAMIC VISUALS
def dimensionConstantSet(arr, x,y):
    '''Updates the constant dimensions used to draw the square arrays.
       Used when the array size changes.                                '''
    global height_interval, width
    # Semi Constants For Box Dimenstions
    height_interval = y / len(arr)
    width = x / len(arr)

    # BEWARE IF VARIABLE, CONSTANTS MAY NOT PRODUCE INTEGERS, POTENTIALLY BREAKING SYSTEM
    
def updateVisual(arr, selected, comparisons):
    screen.fill("Black")    # Resets screen
    staticVisuals()

    # Comparisons
    txt = "#" + str(comparisons) + " Comparisons"
    comp_img = txt_font.render(txt, True, "White")
    screen.blit(comp_img, txt_location)

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
    clock.tick(framerate)


"""Setting up for Game Loop"""
# Creating & Shuffling array to be used by sorting algorithm.
a = createArray(array_size)
a = shuffleArray(a)
dimensionConstantSet(a, useableX, useableY)


"""GAME LOOP"""
sorting = False
updateVisual(a,0,0)
isPlayBTNclicked = False

def playBtnClick():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            distance = math.sqrt((x - play_btn_center[0]) ** 2 + (y - play_btn_center[1]) ** 2)

            if distance <= play_btn_radius:
                print("click detected")
                return True
            
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            distance = math.sqrt((x - play_btn_center[0]) ** 2 + (y - play_btn_center[1]) ** 2)

            if distance <= play_btn_radius:
                isPlayBTNclicked = True
    
    if isPlayBTNclicked and not sorting:
        print("Starting Algoirthm")
        sorting = True
        a = shuffleArray(a)
        bubbleSort(a, updateVisual, playBtnClick) 
    elif isPlayBTNclicked and sorting:
        sorting = False
    
    isPlayBTNclicked = False

    pygame.display.flip()   
    clock.tick(framerate)

pygame.quit()