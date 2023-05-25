import pygame
from modules.plateau import Plateau
from modules.piece import Pieces, Piece

pygame.init = pygame.init
pygame.init()

pygame.MOUSEBUTTONDOWN: int
pygame.QUIT: int
pygame.quit: int

WINDOW_SIZE = (800, 800)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

BLACK_COLOR = (91, 60, 17)
WHITE_COLOR = (200, 173, 127)

board = Plateau(WINDOW, BLACK_COLOR, WHITE_COLOR)
board.draw_background()

king = Piece(4, 0, "king")


PLAYING = True
while PLAYING:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in [king]:
                piece.select_piece()
        if event.type == pygame.QUIT:
            PLAYING = False



    board.draw_lines()

    king.draw(WINDOW, Pieces.black_king)

    for piece in [king]:
        piece.handle()

    pygame.display.flip()

pygame.quit()
