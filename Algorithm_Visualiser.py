#Imports 
import time
import pygame
from Algorithms import bubbleSort, linearSearch
import random
import math
import numpy as np
import pyaudio

"""TODO"""
# TODO : Add algorithms and allow user to change the current algorithm.
# TODO : Polish The implementation
# TODO : The waffle in the features.
# TODO : Add music ...

"""Constants initialisations"""
framerate = 10000
array_size = 50
current_algorithm = linearSearch
launch_with_sorted_array = False

screenX,useableX = 2000, 2000
screenY = 600
useableY = screenY - 50
running = True

play_btn_center = (30,30)
play_btn_radius = 25
txt_location = (play_btn_center[0] + play_btn_radius + 20, play_btn_center[1] - 15)

"""PYGAME initialisations"""
p = pyaudio.PyAudio()
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

def generate_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

def play_tone(frequency, duration):
    wave = generate_tone(frequency, duration)
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)
    stream.write(wave.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()


"""UPDATING VISUALS"""
# DYNAMIC Values
def dimensionConstantSet(arr, x,y):
    '''Updates the constant dimensions used to draw the square arrays.
       Used when the array size changes.                                '''
    global height_interval, width
    # Semi Constants For Box Dimenstions
    height_interval = y / len(arr)
    width = x / len(arr)

    # BEWARE IF VARIABLE, CONSTANTS MAY NOT PRODUCE INTEGERS, POTENTIALLY BREAKING SYSTEM

# DYNAMIC visuals
def updateVisual(arr, selected, metrics):
    global play_btn
    screen.fill("Black")    # Resets screen
    play_btn = pygame.draw.circle(screen, "Green",play_btn_center, play_btn_radius) # Draw the start/stop button

    # Comparisons
    txt = "#" + str(metrics[0]) + " Comparisons" + "   " + "#" + str(metrics[1]) + " Array Accesses"
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

    play_tone(10 * selected+200, 0.1)
    pygame.display.flip()
    clock.tick(framerate)



"""Setting up for Game Loop"""
# Creating & Shuffling array to be used by sorting algorithm.
a = createArray(array_size)
if launch_with_sorted_array:
    a = shuffleArray(a)
dimensionConstantSet(a, useableX, useableY)
updateVisual(a,0,[0,0]) # Initial view of array (sorted or not depending on if shuffled in previous line.)

sorting = False
isPlayBTNclicked = False


"""GAME LOOP"""
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
        # Starting algo or restarting algo
        print("Starting Algoirthm")
        sorting = True
        a = shuffleArray(a)
        current_algorithm(a, updateVisual, playBtnClick)
    elif isPlayBTNclicked and sorting:
        # If the button is clicked and sorting is occuring, stop it. 
        sorting = False
    
    # Ensure that the button is "reset"
    isPlayBTNclicked = False

    pygame.display.flip()   
    clock.tick(framerate)

pygame.quit()