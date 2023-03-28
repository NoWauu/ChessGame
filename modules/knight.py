"""classe des cavaliers"""
import pygame

class Knight:
    """Classe de gestion des cavaliers"""
    def __init__(self) -> None:
        self.white_knight = {
            "knight1": [pygame.image.load("IMG/white/knight.png"), [130, 730], (100, 100)],
            "knight2": [pygame.image.load("IMG/white/knight.png"), [630, 730], (100, 100)]
        }
        self.black_knight = {
            "knight1": [pygame.image.load("IMG/black/knight.png"), [130, 30], (100, 100)],
            "knight2": [pygame.image.load("IMG/black/knight.png"), [630, 30], (100, 100)]
        }

    def place(self, screen: pygame.Surface):
        """place les cavaliers"""
        for knight in self.white_knight.values():
            screen.blit(knight[0], knight[1])
        for knight in self.black_knight.values():
            screen.blit(knight[0], knight[1])

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