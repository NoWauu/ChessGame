import pygame
from modules.plateau import Plateau
from modules.Pieces import Piece, Pawn

pygame.init()

WINDOW_SIZE = (800, 800)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

BLACK_COLOR = (91, 60, 17)
WHITE_COLOR = (200, 173, 127)

board = Plateau(WINDOW, BLACK_COLOR, WHITE_COLOR)
board.draw_background()

playing = True
while playing:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            playing = False


    board.draw_lines()

    board.squares[0] = Piece.queen
    pawn = Pawn(0, 0)
    pawn.draw(WINDOW, Piece.pawn)

    pygame.display.flip()

pygame.quit()