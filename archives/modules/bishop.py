"""classe des fous"""
import pygame

class Bishop:
    """Classe de gestion des fous"""
    def __init__(self, coordinates) -> None:
        self.texture = pygame.image.load("IMG/white/bishop.png")
        self.coordinates = coordinates

    def place(self, screen: pygame.Surface):
        """place les fous"""
        screen.blit(self.texture, self.coordinates)

    def move_diagonal(self, ):
        """déplace le fou en diagonale"""
        pass
