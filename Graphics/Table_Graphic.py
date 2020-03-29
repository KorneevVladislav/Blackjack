import pygame
#import Player_Graphic

def DrawBoard():
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Blackjack")
    screen.fill((0, 255, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

DrawBoard()