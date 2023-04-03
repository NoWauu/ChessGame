"""classe des tours"""
import pygame

class Rook:
    """Classe de gestion des tours"""
    def __init__(self, coordinates) -> None:
        self.texture = pygame.image.load("IMG/white/rook.png")
        self.coordinates = coordinates

    def place(self, screen: pygame.Surface):
        """place les tours"""
        screen.blit(self.texture, self.coordinates)

    def move_horizontal(self, ):
        """déplace la tour horizontalement"""
        pass

    def move_vertical(self, ):
        """déplace la tour verticalement"""
        pass
