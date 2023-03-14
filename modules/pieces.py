import pygame

class Pieces:
    def __init__(self):
        self.is_promotion = False
        self.is_stalemate = False


class WhitePieces(Pieces):
    def __init__(self) -> None:
        self.is_check = False
        self.is_checkmate = False
        self.is_promotion = False

        self.pieces = {
            "king": pygame.image.load("IMG/white/king.png"),
            "queen": pygame.image.load("IMG/white/queen.png"),
            "rook": pygame.image.load("IMG/white/rook.png"),
            "bishop": pygame.image.load("IMG/white/bishop.png"),
            "knight": pygame.image.load("IMG/white/knight.png"),
            "pon": pygame.image.load("IMG/white/pon.png"),
        }

    def draw(self, screen):
        screen.blit(self.pieces["king"], (430, 730))
        screen.blit(self.pieces["queen"], (330, 730))

        screen.blit(self.pieces["rook"], (30, 730))
        screen.blit(self.pieces["rook"], (730, 730))

        screen.blit(self.pieces["bishop"], (230, 730))
        screen.blit(self.pieces["bishop"], (530, 730))

        screen.blit(self.pieces["knight"], (130, 730))
        screen.blit(self.pieces["knight"], (630, 730))

        for i in range(30, 800, 100):
            screen.blit(self.pieces["pon"], (i, 630))

    def move(self):
        pass


class BlackPieces(Pieces):
    """Gestion """
    def __init__(self) -> None:
        self.isCheck = False
        self.isCheckmate = False
        self.isPromotion = False

        self.pieces = {
            "king": pygame.image.load("IMG/black/king.png"),
            "queen": pygame.image.load("IMG/black/queen.png"),
            "rook": pygame.image.load("IMG/black/rook.png"),
            "bishop": pygame.image.load("IMG/black/bishop.png"),
            "knight": pygame.image.load("IMG/black/knight.png"),
            "pon": pygame.image.load("IMG/black/pon.png"),
        }

    def draw(self, screen):
        """mets les pieces noires sur l'échiquier"""
        screen.blit(self.pieces["king"], (430, 30))
        screen.blit(self.pieces["queen"], (330, 30))

        screen.blit(self.pieces["rook"], (30, 30))
        screen.blit(self.pieces["rook"], (730, 30))

        screen.blit(self.pieces["bishop"], (230, 30))
        screen.blit(self.pieces["bishop"], (530, 30))

        screen.blit(self.pieces["knight"], (130, 30))
        screen.blit(self.pieces["knight"], (630, 30))

        for i in range(30, 800, 100):
            screen.blit(self.pieces["pon"], (i, 130))
