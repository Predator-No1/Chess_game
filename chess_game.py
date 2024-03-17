import pygame
"""welcome to the iai chess game not that the command is for the members that doen not understand a certain part
of the  code that is what we need to comment almost every where to avoid amgiguity"""

pygame.init()

WIDTH = 500
HEIGHT = 450

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

#inserting all the game pieces 
blackQueen = pygame.image.load('images/black queen.png')
blackQueen = pygame.transform.scale(blackQueen, (40,40))
blackQueenSmall = pygame.transform.scale(blackQueen, (25,25))

whiteQueen = pygame.image.load('images/white queen.png')
whiteQueen = pygame.transform.scale(whiteQueen, (40,40))
whiteQueenSmall = pygame.transform.scale(whiteQueen, (25,25))

blackKing = pygame.image.load('images/black king.png')
blackKing = pygame.transform.scale(blackKing, (40,40))
blackKingSmall = pygame.transform.scale(blackKing, (25,25))

whiteKing = pygame.image.load('images/white king.png')
whiteKing = pygame.transform.scale(whiteKing, (40,40))
whiteKingSmall = pygame.transform.scale(whiteKing, (25,25))

blackbishop = pygame.image.load('images/black bishop.png')
blackbishop = pygame.transform.scale(blackbishop, (40,40))
blackbishopSmall = pygame.transform.scale(blackbishop, (25,25))

whitebishop = pygame.image.load('images/white bishop.png')
whitebishop = pygame.transform.scale(whitebishop, (40,40))
whitebishopSmall = pygame.transform.scale(whitebishop, (25,25))

blackpawn = pygame.image.load('images/black pawn.png')
blackpawn = pygame.transform.scale(blackpawn, (40,40))
blackpawnSmall = pygame.transform.scale(blackpawn, (25,25))

whitepawn = pygame.image.load('images/white pawn.png')
whitepawn = pygame.transform.scale(whitepawn, (40,40))
whitepawnSmall = pygame.transform.scale(whitepawn, (25,25))

blackrook = pygame.image.load('images/black rook.png')
blackrook = pygame.transform.scale(blackrook, (40,40))
blackrookSmall = pygame.transform.scale(blackrook, (25,25))

whiterook = pygame.image.load('images/white rook.png')
whiterook = pygame.transform.scale(whiterook, (40,40))
whiterookSmall = pygame.transform.scale(whiterook, (25,25))

blackknight = pygame.image.load('images/black knight.png')
blackknight = pygame.transform.scale(blackknight, (40,40))
blackknightSmall = pygame.transform.scale(blackknight, (25,25))

whiteknight = pygame.image.load('images/white knight.png')
whiteknight = pygame.transform.scale(whiteknight, (40,40))
whiteknightSmall = pygame.transform.scale(whiteknight, (25,25))

whiteimages = [whitepawn, whiterook, whiteKing, whiteQueen, whitebishop, whiteknight]
whiteimagessmall = [whitepawnSmall, whiterookSmall, whiteQueenSmall, whiteKingSmall, whitebishopSmall, whiteknightSmall]

blackimages = [blackpawn, blackQueen, blackKing, blackrook, blackbishop, blackknight]
blackimagessmall = [blackpawn, blackQueenSmall, blackknightSmall, blackrookSmall, blackrookSmall, blackknightSmall]

piece_list = ['pawn', 'king', 'queen', 'rook', 'bishop', 'knight']
#main game loop


def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [300 - (column * 100), row * 50, 50, 50])
        else:
            pygame.draw.rect(screen, 'light gray', [350 - (column * 100), row * 50, 50, 50])
continuous = True

while continuous:
    timer.tick(fps)
    screen.fill('dark gray') 
    
    draw_board()
    
    #this is where we will handle the event   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()
    