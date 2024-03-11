import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 900

#setting screen size
screen = pygame.display.set_mode([WIDTH,HEIGHT]) 
pygame.display.set_caption('IAI chess game')

#using a specify font type for the game
font = pygame.font.Font('freesansbold.ttf',20)
timer = pygame.time.Clock()
fps = 60


#main game loop
continuous = True

while continuous:
    timer.tick(fps)
    screen.fill('dark gray') 
    
    #this is where we will handle the event   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()
    