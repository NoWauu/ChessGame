"""classe des reines"""
import pygame

class Queen:
    """Classe de gestion des reines"""
    def __init__(self, coordinates) -> None:
        self.texture = pygame.image.load("IMG/white/queen.png")
        self.coordinates = coordinates

    def place(self, screen: pygame.Surface):
        """place les reines"""
        screen.blit(self.texture, self.coordinates)

    def move_diagonal(self, ):
        """déplace la reine en diagonale"""
        pass

    def move_horizontal(self, ):
        """déplace la reine horizontalement"""
        pass

    def move_vertical(self, ):
        """déplace la reine verticalement"""
        pass