"""classe principale"""
import pygame
from modules.plateau import Plateau
from modules.pieces import Pieces
from modules.pawn import Pawn


pygame.init()

WINDOWSIZE = (830, 830)

WHITECASE_COLOR = (200, 173, 127)
BLACKCASE_COLOR = (91, 60, 17)

FPS = 60

SCREEN = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Chess")

# dessine le plateau
plateau = Plateau(SCREEN, BLACKCASE_COLOR, WHITECASE_COLOR)
plateau.draw_background()
plateau.draw_lines()

# dessine les pieces de base sur le plateau
pieces = Pieces()
pieces.place(SCREEN)

pawn = Pawn()
pawn.place(SCREEN)

PLAYING = True
clock = pygame.time.Clock()
while PLAYING:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAYING = False
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    # actualise l'écran
    pygame.display.flip()

pygame.quit()
