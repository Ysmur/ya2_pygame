import pygame
# инициализация Pygame:
pygame.init()
# размеры окна:
n = int(input())
k = int(input())
size = width, height = n * k * 2, n * k * 2
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# формирование кадра:
# команды рисования на холсте


def draw():
    red = pygame.Color('red')
    blue = pygame.Color('blue')
    green = pygame.Color('green')

    pygame.draw.ellipse(screen, red, )


draw()
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()