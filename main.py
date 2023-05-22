import pygame
from modules.plateau import Plateau
from modules.Pieces import Pieces, Piece

pygame.init()

WINDOW_SIZE = (800, 800)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

BLACK_COLOR = (91, 60, 17)
WHITE_COLOR = (200, 173, 127)

board = Plateau(WINDOW, BLACK_COLOR, WHITE_COLOR)
board.draw_background()

bishop = Piece(5, 6, "bishop")
queen = Piece(4, 1, "queen")
king = Piece(4, 0, "king")

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for piece in [bishop, queen, king]:
                piece.select_piece()
        if event.type == pygame.QUIT:
            playing = False
            


    board.draw_lines()

    bishop.draw(WINDOW, Pieces.white_bishop)
    queen.draw(WINDOW, Pieces.white_queen)
    king.draw(WINDOW, Pieces.black_king)

    for piece in [bishop, queen, king]:
        piece.handle().move()

    pygame.display.flip()

pygame.quit()