import pygame


pygame.init()

WINDOWSIZE = (830, 830)

WHITECASE = (200, 173, 127)
BLACKCASE = (91, 60, 17)

screen = pygame.display.set_mode(WINDOWSIZE)

PLAYING = True
while PLAYING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAYING = False

    pygame.draw.rect(screen, BLACKCASE, (30, 30, WINDOWSIZE[0]-30, WINDOWSIZE[1]-30))
    for x in range(30, WINDOWSIZE[0], 200):
        for y in range(30, WINDOWSIZE[1], 200):
            pygame.draw.rect(screen, WHITECASE, (x, y, 100, 100))
            pygame.draw.rect(screen, WHITECASE, (x + 100, y + 100, 100, 100))

    king = pygame.image.load("IMG/white/king.png")
    queen = pygame.image.load("IMG/white/queen.png")
    rook = pygame.image.load("IMG/white/rook.png")
    bishop = pygame.image.load("IMG/white/bishop.png")
    knight = pygame.image.load("IMG/white/knight.png")
    pon = pygame.image.load("IMG/white/pon.png")

    screen.blit(king, (430, 730))
    screen.blit(queen, (330, 730))

    screen.blit(rook, (30, 730))
    screen.blit(rook, (730, 730))

    screen.blit(bishop, (230, 730))
    screen.blit(bishop, (530, 730))

    screen.blit(knight, (130, 730))
    screen.blit(knight, (630, 730))

    for x in range(30, WINDOWSIZE[0], 100):
        screen.blit(pon, (x, 630))

    king = pygame.image.load("IMG/black/king.png")
    queen = pygame.image.load("IMG/black/queen.png")
    rook = pygame.image.load("IMG/black/rook.png")
    bishop = pygame.image.load("IMG/black/bishop.png")
    knight = pygame.image.load("IMG/black/knight.png")
    pon = pygame.image.load("IMG/black/pon.png")

    screen.blit(king, (430, 30))
    screen.blit(queen, (330, 30))

    screen.blit(rook, (30, 30))
    screen.blit(rook, (730, 30))

    screen.blit(bishop, (230, 30))
    screen.blit(bishop, (530, 30))

    screen.blit(knight, (130, 30))
    screen.blit(knight, (630, 30))

    for x in range(30, WINDOWSIZE[0], 100):
        screen.blit(pon, (x, 130))


    pygame.display.flip()

pygame.quit()
