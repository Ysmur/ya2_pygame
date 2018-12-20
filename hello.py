import pygame

def draw():
    screen.fill(100,0,0)
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
print(1)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
