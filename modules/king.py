"""classe du roi"""
import pygame

class King:
    """Classe de gestion du roi"""
    def __init__(self) -> None:
        self.white_king = {
            "king": [pygame.image.load("IMG/white/king.png"), [430, 730], (100, 100)]
        }
        self.black_king = {
            "king": [pygame.image.load("IMG/black/king.png"), [430, 30], (100, 100)]
        }

    def place(self, screen: pygame.Surface):
        """place les rois"""
        for king in self.white_king.values():
            screen.blit(king[0], king[1])
        for king in self.black_king.values():
            screen.blit(king[0], king[1])

    def move_diagonal(self, ):
        """déplace le roi en diagonale"""
        pass

    def move_horizontal(self, ):
        """déplace le roi horizontalement"""
        pass

    def move_vertical(self, ):
        """déplace le roi verticalement"""
        pass
