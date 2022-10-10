import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Sobrevive UN')
# clock object
clock = pygame.time.Clock()

while True:
    # event loop
    for event in pygame.event.get():
        # input for closing the window
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of init() method
            exit()  # instead of using break is better to use sys module

    pygame.display.update()
    clock.tick(60)