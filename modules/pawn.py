"""classe des pions"""
import pygame

class Pawn:
    """Classe de gestion des pions"""
    def __init__(self) -> None:
        self.white_pawn = {
            "pawn1": [pygame.image.load("IMG/white/pawn.png"), [30, 630], (100, 100)],
            "pawn2": [pygame.image.load("IMG/white/pawn.png"), [130, 630], (100, 100)],
            "pawn3": [pygame.image.load("IMG/white/pawn.png"), [230, 630], (100, 100)],
            "pawn4": [pygame.image.load("IMG/white/pawn.png"), [330, 630], (100, 100)],
            "pawn5": [pygame.image.load("IMG/white/pawn.png"), [430, 630], (100, 100)],
            "pawn6": [pygame.image.load("IMG/white/pawn.png"), [530, 630], (100, 100)],
            "pawn7": [pygame.image.load("IMG/white/pawn.png"), [630, 630], (100, 100)],
            "pawn8": [pygame.image.load("IMG/white/pawn.png"), [730, 630], (100, 100)],
        }

        self.black_pawn = {
            "pawn1": [pygame.image.load("IMG/black/pawn.png"), [30, 130], (100, 100)],
            "pawn2": [pygame.image.load("IMG/black/pawn.png"), [130, 130], (100, 100)],
            "pawn3": [pygame.image.load("IMG/black/pawn.png"), [230, 130], (100, 100)],
            "pawn4": [pygame.image.load("IMG/black/pawn.png"), [330, 130], (100, 100)],
            "pawn5": [pygame.image.load("IMG/black/pawn.png"), [430, 130], (100, 100)],
            "pawn6": [pygame.image.load("IMG/black/pawn.png"), [530, 130], (100, 100)],
            "pawn7": [pygame.image.load("IMG/black/pawn.png"), [630, 130], (100, 100)],
            "pawn8": [pygame.image.load("IMG/black/pawn.png"), [730, 130], (100, 100)],
        }

    def place(self, screen):
        """place les pions sur le plateau"""
        for pawn in self.white_pawn.values():
            screen.blit(self.white_pawn[pawn][0], self.white_pawn[pawn][1])
        for pawn in self.black_pawn.values():
            screen.blit(self.black_pawn[pawn][0], self.black_pawn[pawn][1])

    def move_forward_by_one(self, ):
        """avance le pion d'une case"""
        pass

    def move_forward_by_two(self, ):
        """avance le pion de deux cases"""
        pass

    def eat_diagonal(self, ):
        """mange une piece adverse en diagonale"""
        pass

    def eat_en_passant(self, ):
        """mange une piece adverse en passant"""
        pass

    def promotion(self, ):
        """transforme le pion en une autre piece choisie par le joueur"""
        pass
