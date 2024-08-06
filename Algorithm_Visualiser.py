#Imports 
import time
import pygame
from Algorithms import linearSearch, binarySearch, jumpSearch, exponentialSearch, fibonacciSearch, bogoSearch, bubbleSort, insertionSort, mergeSort, heapSort, countingSort, bogoSort, quickSort
import random
import math
import numpy as np

"""User Defined Variables - Customise to personal liking"""
framerate = 500                  # Advise < 1000 (unlikely pc will be quick enough). Try to match the framerate with the actual to make it more efficient like with games, capping the fps makes it smoother.
array_size = 2500             # Cannot be bigger then the useable X (advised size depends on sorting/searching algorithm used).
current_algorithm = mergeSort      # Pick the current running algo.
launch_with_sorted_array = False     # When the program launches if this is true the array will be shown in its final state, sorted. (If false, array is reshuffled anyway before starting algo (purely aesthetic)).
sorted_array_for_algo = False      # Does the algorithm need a sorted array to run.
disable_sound = False              # Enable/Disable Sound.

screenX,useableX = 2500, 2500       # May need to edit based on monitor, allows bigger array size.
screenY = 600                       # Will effect the jump size between elements

"""Constants initialisations"""
useableY = screenY - 50
running = True

# Calculating constants based on var
height_interval = useableY / array_size
width = useableX / array_size
freq_range = 400

# Sound Calculations 
duration_ms = 100
sample_rate = 44100  # Hertz
n_samples = int(sample_rate * duration_ms / 1000)
t = np.linspace(0, duration_ms / 1000, n_samples, False)
tone_cache = {}

# Button Location
play_btn_center = (30,30)
play_btn_radius = 25
txt_location = (play_btn_center[0] + play_btn_radius + 20, play_btn_center[1] - 15)

"""PYGAME initialisations"""
pygame.init()
screen = pygame.display.set_mode((screenX,screenY))     #Useable 500, 400
pygame.display.set_caption("Algorithm Visualiser")
txt_font = pygame.font.Font(None, 40)
pygame.mixer.init(frequency=44100, size=-16,channels=1, buffer=256)
clock = pygame.time.Clock()


"""Sound Manager"""
# Convert a frequency into a tone
def generate_tone(frequency):

    # Generate a sine wave at the given frequency & convert to 16-bit data      https://en.wikipedia.org/wiki/Sine_wave
    waveform = (32767 * np.sin(2 * np.pi * frequency * t)).astype(np.int16)     # A sin(2pi ft + phase)     - Phase = 0 

    sound = pygame.mixer.Sound(waveform)        # Create sound using pygame mixer.

    return sound

# Calculate the frequency value
def value_to_frequency(value, min_value=1, max_value=array_size, min_freq=0, max_freq=200):
    # Map value to frequency in the given range
    # freq_range * ( corrected_value / value_range)
    return min_freq + (max_freq - min_freq) * ((value - min_value) / (max_value - min_value))

# Add frequency to cache to make it more efficient (so tone is only generated once and then it is just accessed and played)
def get_cached_tone(frequency):
    if frequency not in tone_cache:
        tone_cache[frequency] = generate_tone(frequency)
    
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

        # Sort Colour
        colour = "White"
        if index in selected:
            colour = "Red"


        # Cretae rect & draw to screen
        dimensions = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, colour, dimensions)

    # Play sound
    if not disable_sound:
        frequency = value_to_frequency(arr[selected[0]])
        tone = get_cached_tone(frequency)
        tone.play()

    pygame.display.flip()
    clock.tick(framerate)

# Checks if the array has been sorted.
def finishedVisual(arr, i, green_bars):
    for index, item in enumerate(arr):
        # Calculatre variable dimensions
        height = item * height_interval
        left = index * width
        top = screenY - height

        dimensions = pygame.Rect(left, top, width, height)

        colour = "White"
        if green_bars[index]:
            colour = "Green"
        if item == (i+1) and index == i:
            colour = "Green"
            green_bars[index] = True
        if index == i:
            colour = "Red"


        # Cretae rect & draw to screen
        pygame.draw.rect(screen, colour, dimensions)


    if not disable_sound:
        frequency = value_to_frequency(arr[i])
        tone = generate_tone(frequency)  # 100 ms duration
        tone.play()
    

    pygame.display.flip()
    clock.tick(framerate)


"""Setting up for Game Loop"""
# Creating & Shuffling array to be used by sorting algorithm.
a = createArray(array_size)
if not launch_with_sorted_array:
    a = shuffleArray(a)
updateVisual(a,[0,0],[0,0]) # Initial view of array (sorted or not depending on if shuffled in previous line.)

sorting = False
first_sort = True
isPlayBTNclicked = False


"""GAME LOOP"""
def playBtnClick():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            distance = math.sqrt((x - play_btn_center[0]) ** 2 + (y - play_btn_center[1]) ** 2)

            if distance <= play_btn_radius:
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
        if (not sorted_array_for_algo and launch_with_sorted_array) or (not first_sort and not sorted_array_for_algo):
            a = shuffleArray(a)

        sorting = True
        first_sort = False

        is_sorted = current_algorithm(a, updateVisual, playBtnClick)

        if is_sorted:
            # Show Complete Algorithm
            green_bars = [False] * array_size       # Create an array with false as no bars have been checked.
            for i in range(len(a)):
                if playBtnClick():
                    break
                finishedVisual(a, i, green_bars)
    elif isPlayBTNclicked and sorting:
        # If the button is clicked and sorting is occuring, stop it. 
        sorting = False
    
    # Ensure that the button is "reset"
    isPlayBTNclicked = False

    pygame.display.flip()   
    clock.tick(framerate)

pygame.quit()