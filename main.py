import pygame
from enums import Player


# Variables
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}
colors = [pygame.Color("white"), pygame.Color("gray")]

def load_images():
    for piece in Player.PIECES:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, game_state, valid_moves, square_selected):
    draw_squares(screen)
    highlight_squares(screen, game_state, valid_moves, square_selected)
    draw_pieces(screen, game_state.board)

def draw_squares(screen):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, game_state):
    