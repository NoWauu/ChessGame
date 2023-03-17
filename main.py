import pygame
from modules.pieces import WhitePieces, BlackPieces
from modules.plateau import Plateau


pygame.init()

WINDOWSIZE = (830, 830)

WHITECASE = (200, 173, 127)
BLACKCASE = (91, 60, 17)

FPS = 60

SCREEN = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Chess")

# dessine le plateau
plateau = Plateau(SCREEN, BLACKCASE, WHITECASE)
plateau.draw_background()
plateau.draw_lines()

# place les pièces blanches
pieces_blanches = WhitePieces()
pieces_blanches.draw(SCREEN)

# place les pièces noires
pieces_noires = BlackPieces()
pieces_noires.draw(SCREEN)

# True : blanc / False : noir
turn = True

PLAYING = True
clock = pygame.time.Clock()
while PLAYING:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAYING = False
        if event.type == pygame.MOUSEBUTTONUP:
            pieces_blanches.click()


    # actualise l'écran
    pygame.display.flip()

pygame.quit()
