import pygame
# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = [int(x) for x in input().split()]
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
# формирование кадра:
# команды рисования на холсте


def draw():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, pygame.Color('red'), (1, 1, width - 2, height - 2), 0)

draw()
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()
