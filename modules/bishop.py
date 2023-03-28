"""classe des fous"""
import pygame

class Bishop:
    """Classe de gestion des fous"""
    def __init__(self) -> None:
        self.white_bishop = {
            "bishop_black": [pygame.image.load("IMG/white/bishop.png"), [230, 730], (100, 100)],
            "bishop_white": [pygame.image.load("IMG/white/bishop.png"), [530, 730], (100, 100)]
        }
        self.black_bishop = {
            "bishop_black": [pygame.image.load("IMG/black/bishop.png"), [230, 30], (100, 100)],
            "bishop_white": [pygame.image.load("IMG/black/bishop.png"), [530, 30], (100, 100)]
        }

    def place(self, screen: pygame.Surface):
        """place les fous"""
        for bishop in self.white_bishop.values():
            screen.blit(bishop[0], bishop[1])
        for bishop in self.black_bishop.values():
            screen.blit(bishop[0], bishop[1])

    def move_diagonal(self, ):
        """déplace le fou en diagonale"""
        pass
