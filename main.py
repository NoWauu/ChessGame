import pygame


pygame.init()

WINDOWSIZE = (830, 830)

WHITECASE = (200, 173, 127)
BLACKCASE = (91, 60, 17)

FPS = 60

SCREEN = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Chess")

PLAYING = True
clock = pygame.time.Clock()
while PLAYING:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAYING = False

    pygame.draw.rect(SCREEN, BLACKCASE, (30, 30, WINDOWSIZE[0]-30, WINDOWSIZE[1]-30))
    for x in range(30, WINDOWSIZE[0], 200):
        for y in range(30, WINDOWSIZE[1], 200):
            pygame.draw.rect(SCREEN, WHITECASE, (x, y, 100, 100))
            pygame.draw.rect(SCREEN, WHITECASE, (x + 100, y + 100, 100, 100))

    pygame.display.flip()

pygame.quit()
