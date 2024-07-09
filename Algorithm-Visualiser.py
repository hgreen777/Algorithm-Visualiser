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

class recobj:
    colour = "White"

    x = 0
    y = 0
    top = 0
    left = 0

    def __init__(self, wholeArr, dataObj, left):
        x = screenX / len(wholeArr) 
        y = dataObj * (screenY / len(wholeArr)) 
        top = y
    
    obj = pygame.Rect(left,top,x,y)
    
        
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for index, num in enumerate(testArr):
        left = index * (screenX / len(testArr))
        rec = recobj(testArr, num, left)

        pygame.draw.rect(screen, "White", rec.obj)

    x = screenX / 11
    y = 1 * (screenY / 11)
    top = y
    rec1 = pygame.Rect(5 * (screenX / 10),top,x,y)
    pygame.draw.rect(screen, "White", rec1)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()