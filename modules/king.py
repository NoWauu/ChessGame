"""classe du roi"""
import pygame

class King:
    """Classe de gestion du roi"""
    def __init__(self, coordinates) -> None:

        self.texture = pygame.image.load("IMG/white/king.png")
        self.coordinates = coordinates

    def place(self, screen: pygame.Surface):
        """place les rois"""
        screen.blit(self.texture, self.coordinates)

    def move_diagonal(self, ):
        """déplace le roi en diagonale"""
        pass

    def move_horizontal(self, ):
        """déplace le roi horizontalement"""
        pass

    def move_vertical(self, ):
        """déplace le roi verticalement"""
        pass
