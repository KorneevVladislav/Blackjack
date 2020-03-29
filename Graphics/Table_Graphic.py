import pygame
#import Player_Graphic

def DrawBoard(player_num, player_pos_cards): # both have to be lists so they could be  "hotswaped"
    # Screen is drawn
    screen = pygame.display.set_mode((1920, 1080)) # Need to find screen's resolution and adjust to it. Also need to make the win fill the screen. (square button)
    pygame.display.set_caption("Blackjack")
    screen.fill((0, 255, 0))
    pygame.display.flip()

    # Drawing loop
    while True:
        screen.fill((0, 255, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

DrawBoard(1, 1)