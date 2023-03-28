"""classe des reines"""
import pygame

class Queen:
    """Classe de gestion des reines"""
    def __init__(self) -> None:
        self.white_queen = {
            "queen": [pygame.image.load("IMG/white/queen.png"), [430, 730], (100, 100)]
        }
        self.black_queen = {
            "queen": [pygame.image.load("IMG/black/queen.png"), [430, 30], (100, 100)]
        }

    def place(self, screen: pygame.Surface):
        """place les reines"""
        for queen in self.white_queen.values():
            screen.blit(queen[0], queen[1])
        for queen in self.black_queen.values():
            screen.blit(queen[0], queen[1])

    def move_diagonal(self, ):
        """déplace la reine en diagonale"""
        pass

    def move_horizontal(self, ):
        """déplace la reine horizontalement"""
        pass

    def move_vertical(self, ):
        """déplace la reine verticalement"""
        pass