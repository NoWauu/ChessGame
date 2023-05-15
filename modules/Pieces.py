"""Gestion des pièces"""
import pygame

class Piece:
    none = 0
    king = pygame.image.load("IMG/white/king.png")
    pawn = pygame.image.load("IMG/white/pawn.png")
    knight = pygame.image.load("IMG/white/knight.png")
    bishop = pygame.image.load("IMG/white/bishop.png")
    rook = pygame.image.load("IMG/white/rook.png")
    queen = pygame.image.load("IMG/white/queen.png")

    white = 8
    black = 16



class Pawn(Piece):
    def __init__(self, nb_ligne, nb_col) -> None:
        self.nb_ligne = nb_ligne
        self.nb_col = nb_col
        self.collider = Piece.pawn.get_rect()
        self.can_move_forward_1 = False
        self.can_move_forward_2 = False
        self.selected = False

    def draw(self, screen, texture):
        screen.blit(texture, [0, 0])

    def select_piece(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.collider.collide_point(mouse_pos):
            self.selected = True

    def can_move_forward(self):
        pass

    def move_forward(self, ):
        if self.can_move_forward:
            pass

