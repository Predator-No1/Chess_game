import pygame
"""welcome to the iai chess game not that the command is for the members that doen not understand a certain part
of the  code that is what we need to comment almost every where to avoid amgiguity"""

pygame.init()

WIDTH = 600
HEIGHT = 500

#setting screen size
screen = pygame.display.set_mode([WIDTH,HEIGHT]) 
pygame.display.set_caption('IAI chess game')

#using a specify font type for the game
font = pygame.font.Font('freesansbold.ttf',20)
timer = pygame.time.Clock()
fps = 60

#this are the game variables
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

#turn control
"""i decided to use 4 values :0 for white turn no pieces highlighted 1 for white turn pieces higtlighted
2 for black turn no pieces 3 for blackturn piiece highlighted"""
player_turn = 0

selection = 100

valid_moves = []

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
    