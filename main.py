import pygame

pygame.init()

WINDOWSIZE = (830, 830)
WHITECASE = (200, 173, 127)
BLACKCASE = (91, 60, 17)

screen = pygame.display.set_mode(WINDOWSIZE)

playing = True
while playing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    screen.fill(BLACKCASE)
    for x in range(30, WINDOWSIZE[0], 200):
        for y in range(0, WINDOWSIZE[1], 200):
            pygame.draw.rect(screen, WHITECASE, (x, y, 100, 100))
    for x in range(30, WINDOWSIZE[0], 200):
        for y in range(0, WINDOWSIZE[1], 200):
            pygame.draw.rect(screen, WHITECASE, (x+100, y+100, 100, 100))

    king = pygame.image.load("IMG/king.png")
    queen = pygame.image.load("IMG/queen.png")
    screen.blit(king, (500, 700))
    screen.blit(queen, (400, 700))

    pygame.display.flip()

pygame.quit()