#Imports 
import time
import pygame
import Algorithms

pygame.init()
screenX = 400
screenY = 600
screen = pygame.display.set_mode((screenY,screenX))
pygame.display.set_caption("Algorithm Visualiser")
#Useable 500, 400
clock = pygame.time.Clock()
running = True

testArr = [1,2,3,4,5,6,7,8,9,10]

def dimensionConstantSet(arr, x,y):
    global height_interval, width
    # Semi Constants For Box Dimenstions
    height_interval = y / len(arr)
    width = x / len(arr)

dimensionConstantSet(testArr, screenX, screenY)
    
def updateVisual(arr):
    for index, item in enumerate(arr):
        # Calculatre variable dimensions
        height = item * height_interval
        left = index * width
        top = screenY - height

        # Cretae rect & draw to screen
        dimensions = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, "White", dimensions)

    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    print(pygame.mouse.get_pos())
    updateVisual(testArr)

    pygame.display.flip()

    clock.tick(5)    

pygame.quit()