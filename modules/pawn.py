"""classe des pions"""
import pygame

class Pawn:
    """Classe de gestion des pions"""
    def __init__(self, coordinates) -> None:
        self.texture = pygame.image.load('IMG/white/pawn.png')
        self.coordinates = coordinates
        self.selected = False
        self.rect = self.texture.get_rect().move(self.coordinates)
        print(self.rect)

    def place(self, screen):
        """place les pions sur le plateau"""
        screen.blit(self.texture, self.coordinates)

    def premove_one(self, clicked_area) -> bool:
        if self.rect.collidepoint(clicked_area[0], clicked_area[1]+100):
            return True
        if self.rect.collidepoint(clicked_area) and self.selected is False:
            self.selected = True
        elif self.selected is not False and self.rect.collidepoint(clicked_area[0], clicked_area[1]+100):
            self.selected = False
            return True
        return False


    def premove_two(self, clicked_area):
        if self.rect.collidepoint(clicked_area[0], clicked_area[1]+200):
            return True
        if self.rect.collidepoint(clicked_area) and self.selected is False:
            self.selected = True
        elif self.selected is not False and self.rect.collidepoint(clicked_area[0], clicked_area[1]+200):
            self.selected = False
            return True
        return False

    def move_forward_by_one(self):
        """avance le pion d'une case"""
        """
        si y'a pas de pièce devant:
            avancer (enlever 100 à la coordonée de colonne)
        """
        self.coordinates = [self.coordinates[0], self.coordinates[1] - 100]
        self.rect.centery -= 100

    def move_forward_by_two(self):
        """avance le pion de deux cases"""

        """
        si c'est le premier déplacement (coordonées de ligne = 630):
            regarder si y'a une pièce sur une des deux cases devant
            si non:
                avancer des deux cases (enlever 200 à la coordonnée colonne)
        """
        if self.coordinates[1] == 630:
            self.coordinates[1] -= 200
            self.rect.centery -= 200

    def premove_eat(self, clicked_area):
        if self.rect.collidepoint(clicked_area[0]+100, clicked_area[1]+100):
            return True
        if self.rect.collidepoint(clicked_area) and self.selected is False:
            self.selected = True
        elif self.selected is not False and self.rect.collidepoint(clicked_area[0]+100, clicked_area[1]+100):
            self.selected = False
            return True
        return False

    def eat_diagonal(self, ):
        """mange une piece adverse en diagonale"""
        """
        regarder la pièce en diagonale
        s'il y a une pièce:
            avancer 
        """
        self.coordinates[0] -= 100
        self.coordinates[1] -= 100
        self.rect.centery -= 100
        self.rect.centerx -= 100

    def eat_en_passant(self, ):
        """mange une piece adverse en passant"""
        pass

    def can_promote(self):
        return self.coordinates[1] == 30

    def promotion(self, ):
        """transforme le pion en une autre piece choisie par le joueur"""
        """
        si coordonnée ligne = 30:
            choisir une autre pièce
            self devient instance de la pièce choisie
        """
        print("promotion :)")
            
