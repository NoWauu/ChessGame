"""classe des tours"""
import pygame

class Rook:
    """Classe de gestion des tours"""
    def __init__(self) -> None:
        self.white_rook = {
            "rook1": [pygame.image.load("IMG/white/rook.png"), [30, 730], (100, 100)],
            "rook2": [pygame.image.load("IMG/white/rook.png"), [730, 730], (100, 100)]
        }
        self.black_rook = {
            "rook1": [pygame.image.load("IMG/black/rook.png"), [30, 30], (100, 100)],
            "rook2": [pygame.image.load("IMG/black/rook.png"), [730, 30], (100, 100)]
        }

    def place(self, screen: pygame.Surface):
        """place les tours"""
        for rook in self.white_rook.values():
            screen.blit(rook[0], rook[1])
        for rook in self.black_rook.values():
            screen.blit(rook[0], rook[1])

    def move_horizontal(self, ):
        """déplace la tour horizontalement"""
        pass

    def move_vertical(self, ):
        """déplace la tour verticalement"""
        pass
