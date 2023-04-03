"""classe des cavaliers"""
import pygame

class Knight:
    """Classe de gestion des cavaliers"""
    def __init__(self, coordinates) -> None:
        self.texture = pygame.image.load("IMG/white/knight.png")
        self.coordinates = coordinates

    def place(self, screen: pygame.Surface):
        """place les cavaliers"""
        screen.blit(self.texture, self.coordinates)

    def move_up_right(self, ):
        """déplace le cavalier"""
        pass

    def move_up_left(self, ):
        """déplace le cavalier"""
        pass

    def move_down_right(self, ):
        """déplace le cavalier"""
        pass

    def move_down_left(self, ):
        """déplace le cavalier"""
        pass

    def move_right_up(self, ):
        """déplace le cavalier"""
        pass

    def move_right_down(self, ):
        """déplace le cavalier"""
        pass

    def move_left_up(self, ):
        """déplace le cavalier"""
        pass

    def move_left_down(self, ):
        """déplace le cavalier"""
        pass