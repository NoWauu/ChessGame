"""classe des pièces"""
import pygame

class Pieces:
    """Classe de gestion des pièces"""
    def __init__(self) -> None:
        self.white_pieces = {
            "rook1": [pygame.image.load("IMG/white/rook.png"), [30, 730], (100, 100)],
            "knight1": [pygame.image.load("IMG/white/knight.png"), [130, 730], (100, 100)],
            "bishop_black": [pygame.image.load("IMG/white/bishop.png"), [230, 730], (100, 100)],
            "queen": [pygame.image.load("IMG/white/queen.png"), [330, 730], (100, 100)],
            "king": [pygame.image.load("IMG/white/king.png"), [430, 730], (100, 100)],
            "bishop_white": [pygame.image.load("IMG/white/bishop.png"), [530, 730], (100, 100)],
            "knight2": [pygame.image.load("IMG/white/knight.png"), [630, 730], (100, 100)],
            "rook2": [pygame.image.load("IMG/white/rook.png"), [730, 730], (100, 100)]
        }

        self.black_pieces = {
            "rook1": [pygame.image.load("IMG/black/rook.png"), [30, 30], (100, 100)],
            "knight1": [pygame.image.load("IMG/black/knight.png"), [130, 30], (100, 100)],
            "bishop_black": [pygame.image.load("IMG/black/bishop.png"), [230, 30], (100, 100)],
            "queen": [pygame.image.load("IMG/black/queen.png"), [330, 30], (100, 100)],
            "king": [pygame.image.load("IMG/black/king.png"), [430, 30], (100, 100)],
            "bishop_white": [pygame.image.load("IMG/black/bishop.png"), [530, 30], (100, 100)],
            "knight2": [pygame.image.load("IMG/black/knight.png"), [630, 30], (100, 100)],
            "rook2": [pygame.image.load("IMG/black/rook.png"), [730, 30], (100, 100)]
        }

    def place(self, screen: pygame.Surface):
        """place les pieces de base"""
        for piece in self.white_pieces.values():
            screen.blit(piece[0], piece[1])
        for piece in self.black_pieces.values():
            screen.blit(piece[0], piece[1])
