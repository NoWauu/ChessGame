import pygame

class WhitePieces:
    """Pieces blanches"""
    def __init__(self) -> None:
        self.is_check = False
        self.is_checkmate = False
        self.is_promotion = False
        self.is_turn = True

        self.white_pieces = {
            "king": pygame.image.load("IMG/white/king.png"),
            "queen": pygame.image.load("IMG/white/queen.png"),
            "rook": pygame.image.load("IMG/white/rook.png"),
            "bishop": pygame.image.load("IMG/white/bishop.png"),
            "knight": pygame.image.load("IMG/white/knight.png"),
            "pon": pygame.image.load("IMG/white/pon.png"),
        }

        self.white_positions = {
            "king": (430, 730),
            "queen": (330, 730),
            "rook1": (30, 730),
            "rook2": (730, 730),
            "white_bishop": (230, 730),
            "black_bishop": (530, 730),
            "knight1": (130, 730),
            "knight2": (630, 730),
            "pon1": (30, 630),
            "pon2": (130, 630),
            "pon3": (230, 630),
            "pon4": (330, 630),
            "pon5": (430, 630),
            "pon6": (530, 630),
            "pon7": (630, 630),
            "pon8": (730, 630)
        }

        self.colliders = {
            "king": self.white_pieces["king"].get_rect().move(self.white_positions["king"]),
            "queen": self.white_pieces["queen"].get_rect().move(self.white_positions["queen"]),
            "rook1": self.white_pieces["rook"].get_rect().move(self.white_positions["rook1"]),
            "rook2": self.white_pieces["rook"].get_rect().move(self.white_positions["rook2"]),
            "bishop1": self.white_pieces["bishop"].get_rect().move(self.white_positions["white_bishop"]),
            "bishop2": self.white_pieces["bishop"].get_rect().move(self.white_positions["black_bishop"]),
            "knight1": self.white_pieces["knight"].get_rect().move(self.white_positions["knight1"]),
            "knight2": self.white_pieces["knight"].get_rect().move(self.white_positions["knight2"]),
            "pon1": self.white_pieces["pon"].get_rect().move(self.white_positions["pon1"]),
            "pon2": self.white_pieces["pon"].get_rect().move(self.white_positions["pon2"]),
            "pon3": self.white_pieces["pon"].get_rect().move(self.white_positions["pon3"]),
            "pon4": self.white_pieces["pon"].get_rect().move(self.white_positions["pon4"]),
            "pon5": self.white_pieces["pon"].get_rect().move(self.white_positions["pon5"]),
            "pon6": self.white_pieces["pon"].get_rect().move(self.white_positions["pon6"]),
            "pon7": self.white_pieces["pon"].get_rect().move(self.white_positions["pon7"]),
            "pon8": self.white_pieces["pon"].get_rect().move(self.white_positions["pon8"])
        }

    def draw(self, screen):
        """place les pièces sur l'échiquier"""
        screen.blit(self.white_pieces["king"], (430, 730))
        screen.blit(self.white_pieces["queen"], (330, 730))

        screen.blit(self.white_pieces["rook"], (30, 730))
        screen.blit(self.white_pieces["rook"], (730, 730))

        screen.blit(self.white_pieces["bishop"], (230, 730))
        screen.blit(self.white_pieces["bishop"], (530, 730))

        screen.blit(self.white_pieces["knight"], (130, 730))
        screen.blit(self.white_pieces["knight"], (630, 730))

        for i in range(30, 800, 100):
            screen.blit(self.white_pieces["pon"], (i, 630))

    def click(self):
        """montre les possibilités de déplacement en fonction de la pièce cliquée"""
        # récupère le clic de la souris
        mouse_pos = pygame.mouse.get_pos()
        for piece in self.colliders.values():
            if piece.collidepoint(mouse_pos):
                print(piece)

class BlackPieces:
    """Gestion des pièces noires"""
    def __init__(self) -> None:
        self.is_check = False
        self.is_checkmate = False
        self.is_promotion = False
        self.is_turn = False


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
