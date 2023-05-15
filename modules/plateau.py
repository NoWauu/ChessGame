"""Classe de création du plateau"""
import pygame


class Plateau:
    """Permet de générer le plateau"""
    def __init__(self, screen, blackcase, whitecase):
        self.x_padding = 0
        self.y_padding = 0
        self.screen = screen
        self.blackcase = blackcase
        self.whitecase = whitecase
        self.windowsize = self.screen.get_size()
        self.squares = [0]*64

    def draw_background(self):
        """dessine le fond du plateau"""
        pygame.draw.rect(self.screen, self.blackcase,
                         (self.x_padding, self.y_padding,
                          self.windowsize[0]-self.x_padding,
                          self.windowsize[1]-self.y_padding))

    def draw_lines(self):
        """dessine les cases du plateau"""
        for x_axis in range(self.x_padding, self.windowsize[0], 200):
            for y_axis in range(self.y_padding, self.windowsize[1], 200):
                pygame.draw.rect(self.screen, self.whitecase,
                                 (x_axis, y_axis, 100, 100))
                pygame.draw.rect(self.screen, self.whitecase,
                                 (x_axis + 100, y_axis + 100, 100, 100))
