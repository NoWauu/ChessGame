"""classe principale"""
import pygame
from modules.plateau import Plateau
from modules.pawn import Pawn
from modules.king import King
from modules.rook import Rook
from modules.knight import Knight
from modules.queen import Queen
from modules.bishop import Bishop


pygame.init()

WINDOWSIZE = (830, 830)

WHITECASE_COLOR = (200, 173, 127)
BLACKCASE_COLOR = (91, 60, 17)

FPS = 60

SCREEN = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Chess")

selected = None

# dessine le plateau
plateau = Plateau(SCREEN, BLACKCASE_COLOR, WHITECASE_COLOR)

bishop1 = Bishop([230, 730])
bishop2 = Bishop([530, 730])

queen = Queen([430, 730])

knight1 = Knight([130, 730])
knight2 = Knight([630, 730])

rook1 = Rook([30, 730])
rook2 = Rook([730, 730])

king = King([330, 730])

pawn1 = Pawn([30, 630])
pawn2 = Pawn([130, 630])
pawn3 = Pawn([230, 630])
pawn4 = Pawn([330, 630])
pawn5 = Pawn([430, 630])
pawn6 = Pawn([530, 630])
pawn7 = Pawn([630, 630])
pawn8 = Pawn([730, 630])


PLAYING = True
clock = pygame.time.Clock()
while PLAYING:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAYING = False
        if event.type == pygame.MOUSEBUTTONUP:
            pawn1.premove_one(event.pos)
            if selected == None:
                selected = pawn1.rect
            else:
                selected = None
                pawn1.coordinates = [pawn1.coordinates[0], pawn1.coordinates[1] - 100]
            print(selected)



    plateau.draw_background()
    plateau.draw_lines()

    bishop1.place(SCREEN)
    bishop2.place(SCREEN)
    knight1.place(SCREEN)
    knight2.place(SCREEN)
    king.place(SCREEN)
    queen.place(SCREEN)
    rook1.place(SCREEN)
    rook2.place(SCREEN)

    for pawn in [pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8]:
        pawn.place(SCREEN)

    # actualise l'écran
    pygame.display.flip()

pygame.quit()
