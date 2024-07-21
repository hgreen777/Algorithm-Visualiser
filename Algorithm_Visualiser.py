#Imports 
import time
import pygame
from Algorithms import bubbleSort, linearSearch, binarySearch
import random
import math
import numpy as np

"""TODO"""
# TODO : Add algorithms.
# TODO : Polish The implementation
# TODO : Polish Music (Frequency)

"""Constants initialisations"""
framerate = 5000
array_size = 50    # Cannot be bigger then the useable X
current_algorithm = bubbleSort
launch_with_sorted_array = True
sorted_array_for_algo = False

screenX,useableX = 2500, 2500
screenY = 600
useableY = screenY - 50
running = True

# Calculating constants based on var
height_interval = useableY / array_size
width = useableX / array_size
freq_range = 400
duration_seconds = 1 / framerate
duration_ms = duration_seconds * 1000
if duration_ms < 1:
    duration_ms = 1
tone_cache = {}

play_btn_center = (30,30)
play_btn_radius = 25
txt_location = (play_btn_center[0] + play_btn_radius + 20, play_btn_center[1] - 15)

"""PYGAME initialisations"""
pygame.init()
screen = pygame.display.set_mode((screenX,screenY))     #Useable 500, 400
pygame.display.set_caption("Algorithm Visualiser")
txt_font = pygame.font.Font(None, 40)
pygame.mixer.init(frequency=44100, size=-16, buffer=512)
clock = pygame.time.Clock()

def generate_tone(frequency, duration_ms):
    sample_rate = 44100  # Hertz
    n_samples = int(sample_rate * duration_ms / 1000)
    t = np.linspace(0, duration_ms / 1000, n_samples, False)

    # Generate a sine wave at the given frequency
    waveform = 32767 * np.sin(2 * np.pi * frequency * t)

    # Convert to 16-bit data
    waveform = waveform.astype(np.int16)

    # Ensure waveform is 2D (stereo sound with same values for both channels)
    waveform_stereo = np.column_stack((waveform, waveform))
    sound = pygame.mixer.Sound(waveform)
    return sound


def value_to_frequency(value, min_value, max_value, min_freq=10, max_freq=200):
    # Map value to frequency in the given range
    return min_freq + (max_freq - min_freq) * ((value - min_value) / (max_value - min_value))

def get_cached_tone(frequency):
    if frequency not in tone_cache:
        tone_cache[frequency] = generate_tone(frequency,100)
    
    return tone_cache[frequency]

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
# DYNAMIC visuals
def updateVisual(arr, selected, metrics):    
    global play_btn
    screen.fill("Black")    # Resets screen
    play_btn = pygame.draw.circle(screen, "Green",play_btn_center, play_btn_radius) # Draw the start/stop button

    # Comparisons & Array Access Display
    txt = f"#{metrics[0]} Comparisons   #{metrics[1]} Array Accesses"
    txt_img = txt_font.render(txt, True, "White")
    screen.blit(txt_img, txt_location)

    # FPS Display
    txt = f"{int(clock.get_fps())} FPS"
    txt_img = txt_font.render(txt, True, "Green")
    fps_rect =  txt_img.get_rect(topright=(screenX - 10, 10))
    screen.blit(txt_img,fps_rect)

    '''Updates the visual based of an array at a given point.'''
    for index, item in enumerate(arr):
        # Calculatre variable dimensions
        height = item * height_interval
        left = index * width
        top = screenY - height

        colour = "White"
        if index in selected:
            colour = "Red"


        # Cretae rect & draw to screen
        dimensions = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, colour, dimensions)

    frequency = value_to_frequency(selected[1], 1, len(arr))
    tone = get_cached_tone(frequency)
    tone.play()
    #pygame.time.delay(100)  # Ensure the sound has time to play

    pygame.display.flip()
    clock.tick(framerate)

# vv Purely Visual (doesn't actually check if sorted, jus trust bro)
def finishedVisual(arr, current, flipped):
    total = len(flipped)
    for index, item in enumerate(arr):
        # Calculatre variable dimensions
        height = item * height_interval
        left = index * width
        top = screenY - height

        colour = "White"
        if index <= total:
            colour = "Green"
        if index == current:
            colour = "Red"


        # Cretae rect & draw to screen
        dimensions = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, colour, dimensions)

    frequency = value_to_frequency(current, 1, len(arr))
    tone = generate_tone(frequency, 100)  # 100 ms duration
    tone.play()
    #pygame.time.delay(100)  # Ensure the sound has time to play
    

    pygame.display.flip()
    clock.tick(framerate)


"""Setting up for Game Loop"""
# Creating & Shuffling array to be used by sorting algorithm.
a = createArray(array_size)
if not launch_with_sorted_array:
    a = shuffleArray(a)
updateVisual(a,[0,0],[0,0]) # Initial view of array (sorted or not depending on if shuffled in previous line.)

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
        if not sorted_array_for_algo:
            a = shuffleArray(a)
        is_sorted = current_algorithm(a, updateVisual, playBtnClick)

        if is_sorted:
            allEll = []
            # Show Complete Algorithm
            for i in range(len(a)):
                if playBtnClick():
                    break
                finishedVisual(a, i, allEll)
                allEll.append(i)
    elif isPlayBTNclicked and sorting:
        # If the button is clicked and sorting is occuring, stop it. 
        sorting = False
    
    # Ensure that the button is "reset"
    isPlayBTNclicked = False

    pygame.display.flip()   
    clock.tick(framerate)

pygame.quit()