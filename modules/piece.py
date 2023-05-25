"""Gestion des pièces"""
from math import floor

import pygame


class Pieces:
    white_king = pygame.image.load("IMG/white/king.png")
    white_pawn = pygame.image.load("IMG/white/pawn.png")
    white_knight = pygame.image.load("IMG/white/knight.png")
    white_bishop = pygame.image.load("IMG/white/bishop.png")
    white_rook = pygame.image.load("IMG/white/rook.png")
    white_queen = pygame.image.load("IMG/white/queen.png")

    black_king = pygame.image.load("IMG/black/king.png")
    black_pawn = pygame.image.load("IMG/black/pawn.png")
    black_knight = pygame.image.load("IMG/black/knight.png")
    black_bishop = pygame.image.load("IMG/black/bishop.png")
    black_rook = pygame.image.load("IMG/black/rook.png")
    black_queen = pygame.image.load("IMG/black/queen.png")


class Piece(Pieces):
    def __init__(self, nb_ligne, nb_col, handler) -> None:
        self.nb_ligne = nb_ligne
        self.handler = handler
        self.nb_col = nb_col
        self.can_move_forward_1 = False
        self.can_move_forward_2 = False
        self.selected = False
        self.texture = Pieces.white_king
        self.collider = self.texture.get_rect().move(self.nb_ligne*100, self.nb_col*100)

    def draw(self, screen, texture):
        self.texture = texture
        screen.blit(texture, [self.nb_ligne*100, self.nb_col*100])

    def select_piece(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.collider.collidepoint(mouse_pos):
            self.selected = True
        else:
            self.selected = False

    def handle(self):
        match self.handler:
            case "pawn":
                return Pawn()
            case "bishop":
                return Bishop()
            case "rook":
                return Rook()
            case "queen":
                return Queen()
            case "king":
                return King(self.nb_ligne, self.nb_col, self.handler, self.selected, self.collider)
            case "knight":
                return Knight()
            case _:
                pass



class Pawn(Pieces):
    def __init__(self) -> None:
        super().__init__()

class Rook(Pieces):
    def __init__(self) -> None:
        super().__init__()

class Bishop(Pieces):
    def __init__(self) -> None:
        super().__init__()

    def move(self):
        pass

class Queen(Pieces):
    def __init__(self) -> None:
        super().__init__()

    def move(self):
        pass

class King(Piece):
    def __init__(self, nb_ligne, nb_col, handler, selected, collider) -> None:
        super().__init__(nb_ligne, nb_col, handler)
        self.selected = selected
        self.collider = collider
        print(self.selected)
        if self.selected:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos[0], floor(mouse_pos[0] / 100))
            self.nb_ligne = floor(mouse_pos[0] / 100)
            self.nb_col = floor(mouse_pos[1] / 100)
            self.collider = self.texture.get_rect().move(self.nb_ligne*100, self.nb_col*100)



class Knight(Pieces):
    def __init__(self) -> None:
        super().__init__()
